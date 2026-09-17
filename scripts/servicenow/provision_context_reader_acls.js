(function provisionContextReaderAcls() {

    var ROLE_NAME = 'agentic_context_reader';

    var tableAcls = [
        'sys_script_include',
        'sys_script',
        'sys_script_client',
        'sys_db_object',
        'sys_dictionary'
    ];

    var fieldAcls = [
        'sys_script_include.name',
        'sys_script.name',
        'sys_script_client.name',
        'sys_db_object.name',
        'sys_dictionary.name',
        'sys_dictionary.element'
    ];

    if (!gs.hasRole('security_admin')) {
        gs.error(
            '[Agentic Context] security_admin must be elevated.'
        );
        return;
    }

    var role = new GlideRecord('sys_user_role');
    role.addQuery('name', ROLE_NAME);
    role.setLimit(1);
    role.query();

    if (!role.next()) {
        gs.error(
            '[Agentic Context] Required role not found: ' +
            ROLE_NAME
        );
        return;
    }

    var roleSysId = role.getUniqueValue();

    function ensureReadAcl(name) {

        var acl = new GlideRecord('sys_security_acl');
        acl.addQuery('type', 'record');
        acl.addQuery('operation', 'read');
        acl.addQuery('name', name);
        acl.query();

        while (acl.next()) {

            var existingRole = new GlideRecord(
                'sys_security_acl_role'
            );

            existingRole.addQuery(
                'sys_security_acl',
                acl.getUniqueValue()
            );

            existingRole.addQuery(
                'sys_user_role',
                roleSysId
            );

            existingRole.setLimit(1);
            existingRole.query();

            if (existingRole.next()) {
                gs.print(
                    '[EXISTS] ' + name
                );
                return;
            }
        }

        var newAcl = new GlideRecord(
            'sys_security_acl'
        );

        newAcl.initialize();
        newAcl.setValue('type', 'record');
        newAcl.setValue('operation', 'read');
        newAcl.setValue('name', name);
        newAcl.setValue('active', true);

        var aclSysId = newAcl.insert();

        if (!aclSysId) {
            gs.error(
                '[FAILED] Could not create ACL: ' +
                name
            );
            return;
        }

        var aclRole = new GlideRecord(
            'sys_security_acl_role'
        );

        aclRole.initialize();

        aclRole.setValue(
            'sys_security_acl',
            aclSysId
        );

        aclRole.setValue(
            'sys_user_role',
            roleSysId
        );

        var aclRoleSysId = aclRole.insert();

        if (!aclRoleSysId) {
            gs.error(
                '[PARTIAL FAILURE] ACL created but ' +
                'role mapping failed: ' + name
            );
            return;
        }

        gs.print(
            '[CREATED] ' + name
        );
    }

    for (
        var i = 0;
        i < tableAcls.length;
        i++
    ) {
        ensureReadAcl(
            tableAcls[i]
        );
    }

    for (
        var j = 0;
        j < fieldAcls.length;
        j++
    ) {
        ensureReadAcl(
            fieldAcls[j]
        );
    }

    gs.print(
        '[Agentic Context] ACL provisioning complete.'
    );

})();
