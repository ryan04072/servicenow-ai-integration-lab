import '@servicenow/sdk/global'

declare global {
    namespace Now {
        namespace Internal {
            interface Keys extends KeysRegistry {
                explicit: {
                    bom_json: {
                        table: 'sys_module'
                        id: 'ed8e719b940347a98d255414e7efdada'
                    }
                    package_json: {
                        table: 'sys_module'
                        id: 'c2491501d6314baf994b68713e540485'
                    }
                    src_server_script_ts: {
                        table: 'sys_module'
                        id: '96de82cbeb634cdf940472f9be8e3f1f'
                    }
                }
                composite: [
                    {
                        table: 'sys_db_object'
                        id: '4f2890d03f93460f8f0d90e7258e2a48'
                        key: {
                            name: 'x_1863347_sdkpoc_equipment'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: '558d748065c14dbbaa852a26a0d479e3'
                        key: {
                            name: 'x_1863347_sdkpoc_equipment'
                            element: 'quantity'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: '82a02dfe14664341acdb85a977336763'
                        key: {
                            name: 'x_1863347_sdkpoc_equipment'
                            element: 'NULL'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: '97bd9de797424205aaddbe10d23a5c91'
                        key: {
                            name: 'x_1863347_sdkpoc_equipment'
                            element: 'name'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: '97f5ce8840aa4c84aed03177d2e0d629'
                        key: {
                            name: 'x_1863347_sdkpoc_equipment'
                            element: 'NULL'
                        }
                    },
                    {
                        table: 'ua_table_licensing_config'
                        id: 'a20783e59ee04aae8f230fffe37ed264'
                        key: {
                            name: 'x_1863347_sdkpoc_equipment'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: 'c7d1d20212a44076b0674b4d323e3eed'
                        key: {
                            name: 'x_1863347_sdkpoc_equipment'
                            element: 'description'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: 'c876f4927b8c429da5e05600c1c3b03a'
                        key: {
                            name: 'x_1863347_sdkpoc_equipment'
                            element: 'name'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: 'cc02bbb48e8b4a0890193ed3a40446fc'
                        key: {
                            name: 'x_1863347_sdkpoc_equipment'
                            element: 'quantity'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: 'cf7fbb1b004849f5949211b78b8653ae'
                        key: {
                            name: 'x_1863347_sdkpoc_equipment'
                            element: 'description'
                        }
                    },
                ]
            }
        }
    }
}
