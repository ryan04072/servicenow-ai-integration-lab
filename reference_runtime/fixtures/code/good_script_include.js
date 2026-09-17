var AccessRequestHelper = Class.create();
AccessRequestHelper.prototype = {
    initialize: function() {},

    shouldRequireApplicationOwner: function(requestedItem) {
        if (!requestedItem) {
            return false;
        }
        return requestedItem.u_requires_application_owner === true;
    },

    type: 'AccessRequestHelper'
};
