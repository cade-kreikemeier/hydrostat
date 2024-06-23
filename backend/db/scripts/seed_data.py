from db.models import (
    Crop,
    Device,
    Farm,
    Harvest,
    Role,
    Sensor,
    SensorCalibration,
    SensorInfo,
    SensorReading,
    SensorType,
    Tenant,
    User,
)

tenants: list[Tenant] = [
    {"id": "0ae96c44-7a9f-46f6-bfee-6236d3573b43", "name": "Oxdale"},
    {"id": "5ea5a9b5-1122-4630-98d3-5ce1c00a1b29", "name": "Utopia"},
    {"id": "8a480af3-7c2e-415e-bb3e-e1c18fe7aace", "name": "Basement"},
]

roles: list[Role] = [
    {"id": 1, "name": "Admin"},
    {"id": 2, "name": "User"},
    {"id": 3, "name": "Guest"},
]

users: list[User] = [
    {
        "id": "ed6bdcc1-b785-42c5-9c71-0a53cacbe21f",
        "first_name": "Alice",
        "last_name": "Smith",
        "tenant_id": tenants[0]["id"],
        "role_id": 1,
    },
    {
        "id": "c88c44c8-1f22-4c13-9547-54138e4d5039",
        "first_name": "Bob",
        "last_name": "Doe",
        "tenant_id": tenants[0]["id"],
        "role_id": 2,
    },
    {
        "id": "e1271685-4e82-4aa4-b0e6-a7d29ee55b73",
        "first_name": "Charlie",
        "last_name": "Brown",
        "tenant_id": tenants[0]["id"],
        "role_id": 3,
    },
    {
        "id": "4d2556f1-0f52-430a-9163-3bdd391ab267",
        "first_name": "Ivy",
        "last_name": "Johnson",
        "tenant_id": tenants[1]["id"],
        "role_id": 1,
    },
    {
        "id": "8ce3b2f9-4e2a-45f5-a10b-c793f26bd6e1",
        "first_name": "Liam",
        "last_name": "Doyle",
        "tenant_id": tenants[1]["id"],
        "role_id": 2,
    },
    {
        "id": "89ee91a4-7e3e-448e-91a8-39f96e10cef5",
        "first_name": "Caroline",
        "last_name": "Boyd",
        "tenant_id": tenants[1]["id"],
        "role_id": 3,
    },
    {
        "id": "a977440b-cb1c-4d8e-be41-03fe735b18c9",
        "first_name": "Anna",
        "last_name": "Somers",
        "tenant_id": tenants[2]["id"],
        "role_id": 1,
    },
    {
        "id": "f0bdff4a-8c45-428a-9bd6-75b979e0ecc1",
        "first_name": "Bill",
        "last_name": "Irwin",
        "tenant_id": tenants[2]["id"],
        "role_id": 2,
    },
    {
        "id": "a35a956b-1df2-40fe-bc4c-36b6f1d6f911",
        "first_name": "David",
        "last_name": "Parker",
        "tenant_id": tenants[2]["id"],
        "role_id": 3,
    },
]

farms: list[Farm] = [
    {
        "id": "321ab27a-ff85-48b4-b84c-8e40aaf9865d",
        "name": f"{tenants[0]['name']} Farm 1",
        "tenant_id": tenants[0]["id"],
    },
    {
        "id": "8fcb0e7e-e659-4f2a-bbb7-eba03ca6d607",
        "name": f"{tenants[0]['name']} Farm 2",
        "tenant_id": tenants[0]["id"],
    },
    {
        "id": "3dafcc10-df1a-48d3-a9b9-6d015a698f25",
        "name": f"{tenants[0]['name']} Farm 3",
        "tenant_id": tenants[0]["id"],
    },
    {
        "id": "5adcb75d-a565-4a9d-9070-a669ab4ce6a8",
        "name": f"{tenants[1]['name']} Farm 1",
        "tenant_id": tenants[1]["id"],
    },
    {
        "id": "ad783180-e094-451d-ade7-4db215b17580",
        "name": f"{tenants[1]['name']} Farm 2",
        "tenant_id": tenants[1]["id"],
    },
    {
        "id": "6651e27f-2542-4ec3-815c-21745ebf51df",
        "name": f"{tenants[1]['name']} Farm 3",
        "tenant_id": tenants[1]["id"],
    },
    {
        "id": "6adc1b55-124f-4619-96e3-fb5b1f29a6d6",
        "name": f"{tenants[2]['name']} Farm 1",
        "tenant_id": tenants[2]["id"],
    },
    {
        "id": "97b0d4b3-ae27-4d56-b169-3b0260f409c9",
        "name": f"{tenants[2]['name']} Farm 2",
        "tenant_id": tenants[2]["id"],
    },
    {
        "id": "e177cc75-01c4-4dd6-8543-7695ffce692c",
        "name": f"{tenants[2]['name']} Farm 3",
        "tenant_id": tenants[2]["id"],
    },
]


crops: list[Crop] = [
    {
        "id": "ee9cded9-ed5e-40a8-9381-ea8ac158d59b",
        "name": "Tomato",
        "farm_id": farms[0]["id"],
    },
    {
        "id": "89b434aa-0fb8-4c3a-9b59-6d396dd246cf",
        "name": "Cucumber",
        "farm_id": farms[0]["id"],
    },
    {
        "id": "0e0637cf-903c-4d4d-9784-1406bbfe373d",
        "name": "Carrot",
        "farm_id": farms[1]["id"],
    },
    {
        "id": "c7d4bd27-05c3-48bf-9177-4cc46bda8eaf",
        "name": "Potato",
        "farm_id": farms[1]["id"],
    },
    {
        "id": "a971c1bb-7376-44d1-aeae-7554651ed443",
        "name": "Apple",
        "farm_id": farms[2]["id"],
    },
    {
        "id": "1fbcee32-6bea-4f07-828a-e80ff5bae590",
        "name": "Banana",
        "farm_id": farms[2]["id"],
    },
    {
        "id": "ab014046-01f2-4db4-8884-10fefdc102eb",
        "name": "Orange",
        "farm_id": farms[3]["id"],
    },
    {
        "id": "070f8f13-2d3d-4573-aa4f-d63502e3a040",
        "name": "Grape",
        "farm_id": farms[3]["id"],
    },
    {
        "id": "9990f2a4-bca2-463d-837c-a1b8c04d5c56",
        "name": "Peach",
        "farm_id": farms[4]["id"],
    },
    {
        "id": "23d02b48-0e49-49e9-bb73-7ab97e09947b",
        "name": "Strawberry",
        "farm_id": farms[4]["id"],
    },
    {
        "id": "01747497-2c3d-4533-9bdf-92296f8bd696",
        "name": "Pineapple",
        "farm_id": farms[5]["id"],
    },
    {
        "id": "704000f6-f971-44a2-afe9-ea8425dc7f82",
        "name": "Watermelon",
        "farm_id": farms[5]["id"],
    },
    {
        "id": "48ca5ba2-72cf-480c-b598-c83f4f959137",
        "name": "Mango",
        "farm_id": farms[6]["id"],
    },
    {
        "id": "c3df6442-ce81-4ef0-a9c4-7bfe7ee36ef3",
        "name": "Papaya",
        "farm_id": farms[6]["id"],
    },
    {
        "id": "6cef1a9b-957c-4b7b-a1c1-ec7f77abacb1",
        "name": "Kiwi",
        "farm_id": farms[7]["id"],
    },
    {
        "id": "46fe2e57-5b69-417c-bcf0-42670bc7ebe3",
        "name": "Blueberry",
        "farm_id": farms[7]["id"],
    },
    {
        "id": "0e700efe-a2f1-4396-80b8-5a0727f65e15",
        "name": "Raspberry",
        "farm_id": farms[8]["id"],
    },
    {
        "id": "83032891-3aac-4d4f-a2b5-5c5b41020dea",
        "name": "Blackberry",
        "farm_id": farms[8]["id"],
    },
]

harvests: list[Harvest] = [
    {
        "id": "baa6bfdc-ba46-452b-929a-449216e3789e",
        "date": "2021-01-01T00:00:00+00:00",
        "crop_id": crops[0]["id"],
        "yield_weight": 50,
    },
    {
        "id": "e22c5b23-69ba-4901-a3c6-cbe86fcc7ba1",
        "date": "2021-01-15T00:00:00+00:00",
        "crop_id": crops[0]["id"],
        "yield_weight": 45,
    },
    {
        "id": "d97b17f5-ef15-4b6b-b744-6959f7a2365d",
        "date": "2021-02-01T00:00:00+00:00",
        "crop_id": crops[0]["id"],
        "yield_weight": 60,
    },
    {
        "id": "3f53cea9-5742-47bb-af23-b9de73e9c5cc",
        "date": "2021-01-01T00:00:00+00:00",
        "crop_id": crops[1]["id"],
        "yield_weight": 40,
    },
    {
        "id": "a34b7f8b-f5c9-4c59-b1e1-3a48ac0a046a",
        "date": "2021-01-15T00:00:00+00:00",
        "crop_id": crops[1]["id"],
        "yield_weight": 35,
    },
]


devices: list[Device] = [
    {
        "id": "2791c511-48b5-4f75-a534-e19ac0d4feef",
        "name": "Device 1",
        "crop_id": crops[0]["id"],
    },
    {
        "id": "70dfa67f-e4fe-4ab7-b2b3-a64be2633e65",
        "name": "Device 2",
        "crop_id": crops[0]["id"],
    },
    {
        "id": "b83b1cd6-36a8-4ebc-8ef9-f7865509ef2e",
        "name": "Device 3",
        "crop_id": crops[1]["id"],
    },
    {
        "id": "5ffd7782-429b-4e9c-b7ee-550633e818e2",
        "name": "Device 4",
        "crop_id": crops[1]["id"],
    },
    {
        "id": "83b588f1-f62b-464c-94f0-9bb8f22928d2",
        "name": "Device 5",
        "crop_id": crops[2]["id"],
    },
    {
        "id": "de0acec2-ea49-49c7-b204-52ba8de44114",
        "name": "Device 6",
        "crop_id": crops[2]["id"],
    },
    {
        "id": "9e932134-0683-4947-afaa-3d21f9f6f5ae",
        "name": "Device 7",
        "crop_id": crops[3]["id"],
    },
    {
        "id": "019e43c8-a130-4d83-aa2e-e8b67581d471",
        "name": "Device 8",
        "crop_id": crops[3]["id"],
    },
    {
        "id": "17e59929-2007-4698-adf6-fd9313fb1d7b",
        "name": "Device 9",
        "crop_id": crops[4]["id"],
    },
    {
        "id": "33ad4e9e-465a-4d5e-a1ad-e4abdf7a61f1",
        "name": "Device 10",
        "crop_id": crops[4]["id"],
    },
    {
        "id": "8a67d34f-7f3e-4f5f-a778-ba074147dce6",
        "name": "Device 11",
        "crop_id": crops[5]["id"],
    },
    {
        "id": "0e54a4d5-72d1-4122-b89d-a91550018531",
        "name": "Device 12",
        "crop_id": crops[5]["id"],
    },
    {
        "id": "8608fd93-4c24-445e-8fab-c2d6dea1efdc",
        "name": "Device 13",
        "crop_id": crops[6]["id"],
    },
    {
        "id": "5f1a842b-fdba-42b1-8b52-9e8aedb6a539",
        "name": "Device 14",
        "crop_id": crops[6]["id"],
    },
    {
        "id": "fbdcc3e6-abcd-4a92-b935-a57023d8a06e",
        "name": "Device 15",
        "crop_id": crops[7]["id"],
    },
    {
        "id": "f8772530-9cee-406e-8636-89fd73067a1b",
        "name": "Device 16",
        "crop_id": crops[7]["id"],
    },
    {
        "id": "d785a778-b919-44ea-8793-d258a0edd6a9",
        "name": "Device 17",
        "crop_id": crops[8]["id"],
    },
    {
        "id": "726b0bdd-e014-4d4d-a914-067f2a00161a",
        "name": "Device 18",
        "crop_id": crops[8]["id"],
    },
]


sensor_types: list[SensorType] = [
    {"id": 1, "name": "PH", "unit": "pH"},
    {"id": 2, "name": "TDS", "unit": "ppm"},
    {"id": 3, "name": "Temperature", "unit": "C"},
]


sensor_info: list[SensorInfo] = [
    {
        "id": "aec629d9-df95-48b5-b7d3-ca125e28536c",
        "name": "PH Sensor",
        "manufacturer": "Manufacturer1",
        "model_number": "Model 1",
        "sensor_type_id": sensor_types[0]["id"],
    },
    {
        "id": "a99d1069-8e26-40a8-9589-c0fe619f14eb",
        "name": "TDS Sensor",
        "manufacturer": "Manufacturer1",
        "model_number": "Model 2",
        "sensor_type_id": sensor_types[1]["id"],
    },
    {
        "id": "1ac136c5-4908-4481-b251-74248670c412",
        "name": "Temperature Sensor",
        "manufacturer": "Manufacturer2",
        "model_number": "Model 3",
        "sensor_type_id": sensor_types[2]["id"],
    },
]


sensors: list[Sensor] = [
    {
        "id": "cc64249d-c2ca-4e1f-8e21-3c628f5302dc",
        "name": "PH Sensor",
        "device_id": devices[0]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "ff27e3a0-d8e6-44e4-9b77-131db4d23e18",
        "name": "TDS Sensor",
        "device_id": devices[0]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "40611259-0ea7-423b-a768-c2c3bc579104",
        "name": "Temperature Sensor",
        "device_id": devices[0]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "2acc58f5-7ba4-49b8-b527-810a18e605e1",
        "name": "PH Sensor",
        "device_id": devices[1]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "bb4048a7-cec2-48aa-a5bd-fc379972bc80",
        "name": "TDS Sensor",
        "device_id": devices[1]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "b3e95a09-8524-4be0-aeb8-49710c0daed6",
        "name": "Temperature Sensor",
        "device_id": devices[1]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "aeb31809-2e6e-40fe-b3e0-a2a071b1bf2a",
        "name": "PH Sensor",
        "device_id": devices[2]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "5e04afa7-b9c5-412e-89de-d01441141dc3",
        "name": "TDS Sensor",
        "device_id": devices[2]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "d3b86729-f9a7-4d3e-a8dc-ad65c5778ec1",
        "name": "Temperature Sensor",
        "device_id": devices[2]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "6e73c575-3a3e-4551-8c2c-5e075e09d7ce",
        "name": "PH Sensor",
        "device_id": devices[3]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "7a7a775a-5d90-4173-b132-b9ac08dcf2f9",
        "name": "TDS Sensor",
        "device_id": devices[3]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "96a0cb1c-d6ab-4aa3-93a1-a2995afcfdc1",
        "name": "Temperature Sensor",
        "device_id": devices[3]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "11bd34fc-d9b9-4543-aef7-962c4e6290b1",
        "name": "PH Sensor",
        "device_id": devices[4]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "fd798681-2003-472e-b529-94b7a6071aaa",
        "name": "TDS Sensor",
        "device_id": devices[4]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "7e5a9988-238e-4cf4-9a8d-c0332ec09cf9",
        "name": "Temperature Sensor",
        "device_id": devices[4]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "52743d23-a790-4fac-b08f-980df2db902c",
        "name": "PH Sensor",
        "device_id": devices[5]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "56f4cce9-65c0-4622-b2e4-bb2f779d614e",
        "name": "TDS Sensor",
        "device_id": devices[5]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "5f87971b-2437-4931-a69a-5d7f4381cdb7",
        "name": "Temperature Sensor",
        "device_id": devices[5]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "dfe21831-ac99-4c02-80d0-d53f0a6c2113",
        "name": "PH Sensor",
        "device_id": devices[6]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "bcf4a06a-0d78-4169-8e07-b4cc68c82975",
        "name": "TDS Sensor",
        "device_id": devices[6]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "78837596-074f-4dad-a9aa-343ed69d0852",
        "name": "Temperature Sensor",
        "device_id": devices[6]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "449f90b5-a9d7-47d3-a5b0-c89f3d4011f6",
        "name": "PH Sensor",
        "device_id": devices[7]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "8d73e8c0-cdb7-4926-8e1a-10155eb9984b",
        "name": "TDS Sensor",
        "device_id": devices[7]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "50c53ee7-9d5a-49e7-8ad1-162053de57fc",
        "name": "Temperature Sensor",
        "device_id": devices[7]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "255dc460-9e2b-4027-9330-0cde272cd261",
        "name": "PH Sensor",
        "device_id": devices[8]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "5e11a401-ee3d-4f34-bbba-93d5ba7972bb",
        "name": "TDS Sensor",
        "device_id": devices[8]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "00f81340-d3f2-4e82-9580-8ad0c2301e80",
        "name": "Temperature Sensor",
        "device_id": devices[8]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "39518e5c-8ebe-4671-8495-f8f7802dec41",
        "name": "PH Sensor",
        "device_id": devices[9]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "46c70bc7-2339-4f87-9961-b72ca3fc5464",
        "name": "TDS Sensor",
        "device_id": devices[9]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "00137b38-2cc0-434f-a885-68eb60fad3b2",
        "name": "Temperature Sensor",
        "device_id": devices[9]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "6b521ee0-8196-46e6-87b3-5b4ed7301362",
        "name": "PH Sensor",
        "device_id": devices[10]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "0e87012b-f8cf-4109-bcb4-cdc84103042e",
        "name": "TDS Sensor",
        "device_id": devices[10]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "8a1f14bb-10ac-4d12-a98a-c68c1c1b8437",
        "name": "Temperature Sensor",
        "device_id": devices[10]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "ad5ead83-3c17-4aa9-a84f-9ec033aabb7b",
        "name": "PH Sensor",
        "device_id": devices[11]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "b15a616f-e9a9-4a39-bbe4-19910e507f19",
        "name": "TDS Sensor",
        "device_id": devices[11]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "1dfc5bc1-8e23-4e38-87ee-802121e69fb8",
        "name": "Temperature Sensor",
        "device_id": devices[11]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "d6e6534d-5d79-4f00-8bdc-8cca53ab9fa9",
        "name": "PH Sensor",
        "device_id": devices[12]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "889c3c64-7bc6-4c0a-9563-b4f326e26339",
        "name": "TDS Sensor",
        "device_id": devices[12]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "2722c18e-59e7-42cb-af42-62de38ad132d",
        "name": "Temperature Sensor",
        "device_id": devices[12]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "bd7e0fc4-5f27-4e21-9f40-672f9cf1337a",
        "name": "PH Sensor",
        "device_id": devices[13]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "f14d0bc7-97e8-4dd4-b061-03cbe364089d",
        "name": "TDS Sensor",
        "device_id": devices[13]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "f4b1bd32-4cc2-4ac4-92b4-46eea9b2ff8a",
        "name": "Temperature Sensor",
        "device_id": devices[13]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "00faff30-3adb-454a-abd2-04044f7ed8e4",
        "name": "PH Sensor",
        "device_id": devices[14]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "90668cf2-e3d3-453c-8512-54b767580f28",
        "name": "TDS Sensor",
        "device_id": devices[14]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "5784c441-c06a-425d-8868-0dccb033edbd",
        "name": "Temperature Sensor",
        "device_id": devices[14]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "458d8832-6ae2-4907-8a62-99c782a0643b",
        "name": "PH Sensor",
        "device_id": devices[15]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "ffae8e34-cff3-4230-ad86-6a7931531e33",
        "name": "TDS Sensor",
        "device_id": devices[15]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "11d5d254-2a1d-4446-8b7d-2d3c401622a2",
        "name": "Temperature Sensor",
        "device_id": devices[15]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "75ceab8b-5589-45c0-b7ce-4ed3151390de",
        "name": "PH Sensor",
        "device_id": devices[16]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "fa8fd0d1-3504-42dc-9d09-004979a0b6e5",
        "name": "TDS Sensor",
        "device_id": devices[16]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "a61a6fdf-c373-4345-8d46-03b272cb0b1c",
        "name": "Temperature Sensor",
        "device_id": devices[16]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
    {
        "id": "8d289129-59ca-4e63-9a7c-a6953ad8ff85",
        "name": "PH Sensor",
        "device_id": devices[17]["id"],
        "sensor_info_id": sensor_info[0]["id"],
    },
    {
        "id": "e81d3f93-08c5-42f1-8bad-dc354afc551a",
        "name": "TDS Sensor",
        "device_id": devices[17]["id"],
        "sensor_info_id": sensor_info[1]["id"],
    },
    {
        "id": "a7c69c86-7d6f-4b58-9e24-b5ad489b1460",
        "name": "Temperature Sensor",
        "device_id": devices[17]["id"],
        "sensor_info_id": sensor_info[2]["id"],
    },
]

sensor_calibrations: list[SensorCalibration] = [
    {
        "id": 1,
        "date": "2024-01-01 00:00:00",
        "calibration_pass": True,
        "sensor_id": sensors[0]["id"],
    },
    {
        "id": 2,
        "date": "2024-01-08 00:00:00",
        "calibration_pass": False,
        "sensor_id": sensors[0]["id"],
    },
    {
        "id": 3,
        "date": "2024-01-15 00:00:00",
        "calibration_pass": True,
        "sensor_id": sensors[0]["id"],
    },
    {
        "id": 4,
        "date": "2024-01-01 00:00:00",
        "calibration_pass": True,
        "sensor_id": sensors[1]["id"],
    },
    {
        "id": 5,
        "date": "2024-01-08 00:00:00",
        "calibration_pass": False,
        "sensor_id": sensors[1]["id"],
    },
    {
        "id": 6,
        "date": "2024-01-15 00:00:00",
        "calibration_pass": True,
        "sensor_id": sensors[1]["id"],
    },
    {
        "id": 7,
        "date": "2024-01-01 00:00:00",
        "calibration_pass": True,
        "sensor_id": sensors[2]["id"],
    },
    {
        "id": 8,
        "date": "2024-01-08 00:00:00",
        "calibration_pass": False,
        "sensor_id": sensors[2]["id"],
    },
    {
        "id": 9,
        "date": "2024-01-15 00:00:00",
        "calibration_pass": True,
        "sensor_id": sensors[2]["id"],
    },
]

sensor_readings: list[SensorReading] = [
    {
        "id": 1,
        "date": "2024-01-15 00:00:00",
        "value": 7.0,
        "sensor_id": sensors[0]["id"],
    },
    {
        "id": 2,
        "date": "2024-01-15 00:10:00",
        "value": 7.1,
        "sensor_id": sensors[0]["id"],
    },
    {
        "id": 3,
        "date": "2024-01-15 00:20:00",
        "value": 6.8,
        "sensor_id": sensors[0]["id"],
    },
    {
        "id": 4,
        "date": "2024-01-15 00:00:00",
        "value": 500.0,
        "sensor_id": sensors[1]["id"],
    },
    {
        "id": 5,
        "date": "2024-01-15 00:10:00",
        "value": 487.9,
        "sensor_id": sensors[1]["id"],
    },
    {
        "id": 6,
        "date": "2024-01-15 00:20:00",
        "value": 510.32,
        "sensor_id": sensors[1]["id"],
    },
    {
        "id": 7,
        "date": "2024-01-15 00:00:00",
        "value": 25.0,
        "sensor_id": sensors[2]["id"],
    },
    {
        "id": 8,
        "date": "2024-01-15 00:10:00",
        "value": 24.2,
        "sensor_id": sensors[2]["id"],
    },
    {
        "id": 9,
        "date": "2024-01-15 00:20:00",
        "value": 25.4,
        "sensor_id": sensors[2]["id"],
    },
]
