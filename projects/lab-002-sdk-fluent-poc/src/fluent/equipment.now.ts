import { IntegerColumn, StringColumn, Table } from '@servicenow/sdk/core'

export const x_1863347_sdkpoc_equipment = Table({
    name: 'x_1863347_sdkpoc_equipment',
    label: 'SDK POC Equipment',
    display: 'name',
    schema: {
        name: StringColumn({
            label: 'Name',
            maxLength: 120,
            mandatory: true,
        }),
        description: StringColumn({
            label: 'Description',
            maxLength: 255,
        }),
        quantity: IntegerColumn({
            label: 'Quantity',
        }),
    },
})
