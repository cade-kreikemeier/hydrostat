CREATE TABLE public."Tenants" (
        id UUID NOT NULL,
        name VARCHAR(50) NOT NULL,
        address VARCHAR(50),
        contact_email VARCHAR(50),
        PRIMARY KEY (id)
);


CREATE TABLE public."Roles" (
        id SERIAL NOT NULL,
        name VARCHAR(50) NOT NULL,
        PRIMARY KEY (id)
);


CREATE TABLE public."SensorTypes" (
        id SERIAL NOT NULL,
        name VARCHAR(50) NOT NULL,
        unit VARCHAR(8) NOT NULL,
        PRIMARY KEY (id)
);


CREATE TABLE public."Users" (
        id UUID NOT NULL,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        middle_initial VARCHAR(1),
        role_id INTEGER NOT NULL,
        tenant_id UUID NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(role_id) REFERENCES "Roles" (id),
        FOREIGN KEY(tenant_id) REFERENCES "Tenants" (id)
);


CREATE TABLE public."Farms" (
        id UUID NOT NULL,
        name VARCHAR(50) NOT NULL,
        location VARCHAR(50),
        tenant_id UUID NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(tenant_id) REFERENCES "Tenants" (id)
);


CREATE TABLE public."SensorInfo" (
        id UUID NOT NULL,
        name VARCHAR(50) NOT NULL,
        manufacturer VARCHAR(50) NOT NULL,
        model_number VARCHAR(50) NOT NULL,
        sensor_type_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(sensor_type_id) REFERENCES "SensorTypes" (id)
);


CREATE TABLE public."Crops" (
        id UUID NOT NULL,
        name VARCHAR(50) NOT NULL,
        farm_id UUID NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(farm_id) REFERENCES "Farms" (id)
);


CREATE TABLE public."Harvests" (
        id UUID NOT NULL,
        date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        crop_id UUID NOT NULL,
        yield_weight INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(crop_id) REFERENCES "Crops" (id)
);


CREATE TABLE public."Devices" (
        id UUID NOT NULL,
        name VARCHAR(50) NOT NULL,
        crop_id UUID,
        PRIMARY KEY (id),
        FOREIGN KEY(crop_id) REFERENCES "Crops" (id)
);


CREATE TABLE public."Sensors" (
        id UUID NOT NULL,
        name VARCHAR(50) NOT NULL,
        device_id UUID NOT NULL,
        sensor_info_id UUID NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(device_id) REFERENCES "Devices" (id),
        FOREIGN KEY(sensor_info_id) REFERENCES "SensorInfo" (id)
);


CREATE TABLE public."SensorCalibrations" (
        id SERIAL NOT NULL,
        date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        calibration_pass BOOLEAN NOT NULL,
        sensor_id UUID NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(sensor_id) REFERENCES "Sensors" (id)
);


CREATE TABLE public."SensorReadings" (
        id SERIAL NOT NULL,
        date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        value REAL NOT NULL,
        sensor_id UUID NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(sensor_id) REFERENCES "Sensors" (id)
);


COPY public."Tenants" (id, name, address, contact_email) FROM stdin;
0ae96c44-7a9f-46f6-bfee-6236d3573b43	Oxdale	\N	\N
5ea5a9b5-1122-4630-98d3-5ce1c00a1b29	Utopia	\N	\N
8a480af3-7c2e-415e-bb3e-e1c18fe7aace	Basement	\N	\N
\.


COPY public."Roles" (id, name) FROM stdin;
1	Admin
2	User
3	Guest
\.


COPY public."SensorTypes" (id, name, unit) FROM stdin;
1	PH	pH
2	TDS	ppm
3	Temperature	C
\.


COPY public."Users" (id, first_name, last_name, middle_initial, role_id, tenant_id) FROM stdin;
ed6bdcc1-b785-42c5-9c71-0a53cacbe21f	Alice	Smith	\N	1	0ae96c44-7a9f-46f6-bfee-6236d3573b43
c88c44c8-1f22-4c13-9547-54138e4d5039	Bob	Doe	\N	2	0ae96c44-7a9f-46f6-bfee-6236d3573b43
e1271685-4e82-4aa4-b0e6-a7d29ee55b73	Charlie	Brown	\N	3	0ae96c44-7a9f-46f6-bfee-6236d3573b43
4d2556f1-0f52-430a-9163-3bdd391ab267	Ivy	Johnson	\N	1	5ea5a9b5-1122-4630-98d3-5ce1c00a1b29
8ce3b2f9-4e2a-45f5-a10b-c793f26bd6e1	Liam	Doyle	\N	2	5ea5a9b5-1122-4630-98d3-5ce1c00a1b29
89ee91a4-7e3e-448e-91a8-39f96e10cef5	Caroline	Boyd	\N	3	5ea5a9b5-1122-4630-98d3-5ce1c00a1b29
a977440b-cb1c-4d8e-be41-03fe735b18c9	Anna	Somers	\N	1	8a480af3-7c2e-415e-bb3e-e1c18fe7aace
f0bdff4a-8c45-428a-9bd6-75b979e0ecc1	Bill	Irwin	\N	2	8a480af3-7c2e-415e-bb3e-e1c18fe7aace
a35a956b-1df2-40fe-bc4c-36b6f1d6f911	David	Parker	\N	3	8a480af3-7c2e-415e-bb3e-e1c18fe7aace
\.


COPY public."Farms" (id, name, location, tenant_id) FROM stdin;
321ab27a-ff85-48b4-b84c-8e40aaf9865d	Oxdale Farm 1	\N	0ae96c44-7a9f-46f6-bfee-6236d3573b43
8fcb0e7e-e659-4f2a-bbb7-eba03ca6d607	Oxdale Farm 2	\N	0ae96c44-7a9f-46f6-bfee-6236d3573b43
3dafcc10-df1a-48d3-a9b9-6d015a698f25	Oxdale Farm 3	\N	0ae96c44-7a9f-46f6-bfee-6236d3573b43
5adcb75d-a565-4a9d-9070-a669ab4ce6a8	Utopia Farm 1	\N	5ea5a9b5-1122-4630-98d3-5ce1c00a1b29
ad783180-e094-451d-ade7-4db215b17580	Utopia Farm 2	\N	5ea5a9b5-1122-4630-98d3-5ce1c00a1b29
6651e27f-2542-4ec3-815c-21745ebf51df	Utopia Farm 3	\N	5ea5a9b5-1122-4630-98d3-5ce1c00a1b29
6adc1b55-124f-4619-96e3-fb5b1f29a6d6	Basement Farm 1	\N	8a480af3-7c2e-415e-bb3e-e1c18fe7aace
97b0d4b3-ae27-4d56-b169-3b0260f409c9	Basement Farm 2	\N	8a480af3-7c2e-415e-bb3e-e1c18fe7aace
e177cc75-01c4-4dd6-8543-7695ffce692c	Basement Farm 3	\N	8a480af3-7c2e-415e-bb3e-e1c18fe7aace
\.


COPY public."SensorInfo" (id, name, manufacturer, model_number, sensor_type_id) FROM stdin;
aec629d9-df95-48b5-b7d3-ca125e28536c	PH Sensor	Manufacturer1	Model 1	1
a99d1069-8e26-40a8-9589-c0fe619f14eb	TDS Sensor	Manufacturer1	Model 2	2
1ac136c5-4908-4481-b251-74248670c412	Temperature Sensor	Manufacturer2	Model 3	3
\.


COPY public."Crops" (id, name, farm_id) FROM stdin;
ee9cded9-ed5e-40a8-9381-ea8ac158d59b	Tomato	321ab27a-ff85-48b4-b84c-8e40aaf9865d
89b434aa-0fb8-4c3a-9b59-6d396dd246cf	Cucumber	321ab27a-ff85-48b4-b84c-8e40aaf9865d
0e0637cf-903c-4d4d-9784-1406bbfe373d	Carrot	8fcb0e7e-e659-4f2a-bbb7-eba03ca6d607
c7d4bd27-05c3-48bf-9177-4cc46bda8eaf	Potato	8fcb0e7e-e659-4f2a-bbb7-eba03ca6d607
a971c1bb-7376-44d1-aeae-7554651ed443	Apple	3dafcc10-df1a-48d3-a9b9-6d015a698f25
1fbcee32-6bea-4f07-828a-e80ff5bae590	Banana	3dafcc10-df1a-48d3-a9b9-6d015a698f25
ab014046-01f2-4db4-8884-10fefdc102eb	Orange	5adcb75d-a565-4a9d-9070-a669ab4ce6a8
070f8f13-2d3d-4573-aa4f-d63502e3a040	Grape	5adcb75d-a565-4a9d-9070-a669ab4ce6a8
9990f2a4-bca2-463d-837c-a1b8c04d5c56	Peach	ad783180-e094-451d-ade7-4db215b17580
23d02b48-0e49-49e9-bb73-7ab97e09947b	Strawberry	ad783180-e094-451d-ade7-4db215b17580
01747497-2c3d-4533-9bdf-92296f8bd696	Pineapple	6651e27f-2542-4ec3-815c-21745ebf51df
704000f6-f971-44a2-afe9-ea8425dc7f82	Watermelon	6651e27f-2542-4ec3-815c-21745ebf51df
48ca5ba2-72cf-480c-b598-c83f4f959137	Mango	6adc1b55-124f-4619-96e3-fb5b1f29a6d6
c3df6442-ce81-4ef0-a9c4-7bfe7ee36ef3	Papaya	6adc1b55-124f-4619-96e3-fb5b1f29a6d6
6cef1a9b-957c-4b7b-a1c1-ec7f77abacb1	Kiwi	97b0d4b3-ae27-4d56-b169-3b0260f409c9
46fe2e57-5b69-417c-bcf0-42670bc7ebe3	Blueberry	97b0d4b3-ae27-4d56-b169-3b0260f409c9
0e700efe-a2f1-4396-80b8-5a0727f65e15	Raspberry	e177cc75-01c4-4dd6-8543-7695ffce692c
83032891-3aac-4d4f-a2b5-5c5b41020dea	Blackberry	e177cc75-01c4-4dd6-8543-7695ffce692c
\.


COPY public."Harvests" (id, date, crop_id, yield_weight) FROM stdin;
baa6bfdc-ba46-452b-929a-449216e3789e	2021-01-01 00:00:00	ee9cded9-ed5e-40a8-9381-ea8ac158d59b	50
e22c5b23-69ba-4901-a3c6-cbe86fcc7ba1	2021-01-15 00:00:00	ee9cded9-ed5e-40a8-9381-ea8ac158d59b	45
d97b17f5-ef15-4b6b-b744-6959f7a2365d	2021-02-01 00:00:00	ee9cded9-ed5e-40a8-9381-ea8ac158d59b	60
3f53cea9-5742-47bb-af23-b9de73e9c5cc	2021-01-01 00:00:00	89b434aa-0fb8-4c3a-9b59-6d396dd246cf	40
a34b7f8b-f5c9-4c59-b1e1-3a48ac0a046a	2021-01-15 00:00:00	89b434aa-0fb8-4c3a-9b59-6d396dd246cf	35
\.


COPY public."Devices" (id, name, crop_id) FROM stdin;
2791c511-48b5-4f75-a534-e19ac0d4feef	Device 1	ee9cded9-ed5e-40a8-9381-ea8ac158d59b
70dfa67f-e4fe-4ab7-b2b3-a64be2633e65	Device 2	ee9cded9-ed5e-40a8-9381-ea8ac158d59b
b83b1cd6-36a8-4ebc-8ef9-f7865509ef2e	Device 3	89b434aa-0fb8-4c3a-9b59-6d396dd246cf
5ffd7782-429b-4e9c-b7ee-550633e818e2	Device 4	89b434aa-0fb8-4c3a-9b59-6d396dd246cf
83b588f1-f62b-464c-94f0-9bb8f22928d2	Device 5	0e0637cf-903c-4d4d-9784-1406bbfe373d
de0acec2-ea49-49c7-b204-52ba8de44114	Device 6	0e0637cf-903c-4d4d-9784-1406bbfe373d
9e932134-0683-4947-afaa-3d21f9f6f5ae	Device 7	c7d4bd27-05c3-48bf-9177-4cc46bda8eaf
019e43c8-a130-4d83-aa2e-e8b67581d471	Device 8	c7d4bd27-05c3-48bf-9177-4cc46bda8eaf
17e59929-2007-4698-adf6-fd9313fb1d7b	Device 9	a971c1bb-7376-44d1-aeae-7554651ed443
33ad4e9e-465a-4d5e-a1ad-e4abdf7a61f1	Device 10	a971c1bb-7376-44d1-aeae-7554651ed443
8a67d34f-7f3e-4f5f-a778-ba074147dce6	Device 11	1fbcee32-6bea-4f07-828a-e80ff5bae590
0e54a4d5-72d1-4122-b89d-a91550018531	Device 12	1fbcee32-6bea-4f07-828a-e80ff5bae590
8608fd93-4c24-445e-8fab-c2d6dea1efdc	Device 13	ab014046-01f2-4db4-8884-10fefdc102eb
5f1a842b-fdba-42b1-8b52-9e8aedb6a539	Device 14	ab014046-01f2-4db4-8884-10fefdc102eb
fbdcc3e6-abcd-4a92-b935-a57023d8a06e	Device 15	070f8f13-2d3d-4573-aa4f-d63502e3a040
f8772530-9cee-406e-8636-89fd73067a1b	Device 16	070f8f13-2d3d-4573-aa4f-d63502e3a040
d785a778-b919-44ea-8793-d258a0edd6a9	Device 17	9990f2a4-bca2-463d-837c-a1b8c04d5c56
726b0bdd-e014-4d4d-a914-067f2a00161a	Device 18	9990f2a4-bca2-463d-837c-a1b8c04d5c56
\.


COPY public."Sensors" (id, name, device_id, sensor_info_id) FROM stdin;
cc64249d-c2ca-4e1f-8e21-3c628f5302dc	PH Sensor	2791c511-48b5-4f75-a534-e19ac0d4feef	aec629d9-df95-48b5-b7d3-ca125e28536c
ff27e3a0-d8e6-44e4-9b77-131db4d23e18	TDS Sensor	2791c511-48b5-4f75-a534-e19ac0d4feef	a99d1069-8e26-40a8-9589-c0fe619f14eb
40611259-0ea7-423b-a768-c2c3bc579104	Temperature Sensor	2791c511-48b5-4f75-a534-e19ac0d4feef	1ac136c5-4908-4481-b251-74248670c412
2acc58f5-7ba4-49b8-b527-810a18e605e1	PH Sensor	70dfa67f-e4fe-4ab7-b2b3-a64be2633e65	aec629d9-df95-48b5-b7d3-ca125e28536c
bb4048a7-cec2-48aa-a5bd-fc379972bc80	TDS Sensor	70dfa67f-e4fe-4ab7-b2b3-a64be2633e65	a99d1069-8e26-40a8-9589-c0fe619f14eb
b3e95a09-8524-4be0-aeb8-49710c0daed6	Temperature Sensor	70dfa67f-e4fe-4ab7-b2b3-a64be2633e65	1ac136c5-4908-4481-b251-74248670c412
aeb31809-2e6e-40fe-b3e0-a2a071b1bf2a	PH Sensor	b83b1cd6-36a8-4ebc-8ef9-f7865509ef2e	aec629d9-df95-48b5-b7d3-ca125e28536c
5e04afa7-b9c5-412e-89de-d01441141dc3	TDS Sensor	b83b1cd6-36a8-4ebc-8ef9-f7865509ef2e	a99d1069-8e26-40a8-9589-c0fe619f14eb
d3b86729-f9a7-4d3e-a8dc-ad65c5778ec1	Temperature Sensor	b83b1cd6-36a8-4ebc-8ef9-f7865509ef2e	1ac136c5-4908-4481-b251-74248670c412
6e73c575-3a3e-4551-8c2c-5e075e09d7ce	PH Sensor	5ffd7782-429b-4e9c-b7ee-550633e818e2	aec629d9-df95-48b5-b7d3-ca125e28536c
7a7a775a-5d90-4173-b132-b9ac08dcf2f9	TDS Sensor	5ffd7782-429b-4e9c-b7ee-550633e818e2	a99d1069-8e26-40a8-9589-c0fe619f14eb
96a0cb1c-d6ab-4aa3-93a1-a2995afcfdc1	Temperature Sensor	5ffd7782-429b-4e9c-b7ee-550633e818e2	1ac136c5-4908-4481-b251-74248670c412
11bd34fc-d9b9-4543-aef7-962c4e6290b1	PH Sensor	83b588f1-f62b-464c-94f0-9bb8f22928d2	aec629d9-df95-48b5-b7d3-ca125e28536c
fd798681-2003-472e-b529-94b7a6071aaa	TDS Sensor	83b588f1-f62b-464c-94f0-9bb8f22928d2	a99d1069-8e26-40a8-9589-c0fe619f14eb
7e5a9988-238e-4cf4-9a8d-c0332ec09cf9	Temperature Sensor	83b588f1-f62b-464c-94f0-9bb8f22928d2	1ac136c5-4908-4481-b251-74248670c412
52743d23-a790-4fac-b08f-980df2db902c	PH Sensor	de0acec2-ea49-49c7-b204-52ba8de44114	aec629d9-df95-48b5-b7d3-ca125e28536c
56f4cce9-65c0-4622-b2e4-bb2f779d614e	TDS Sensor	de0acec2-ea49-49c7-b204-52ba8de44114	a99d1069-8e26-40a8-9589-c0fe619f14eb
5f87971b-2437-4931-a69a-5d7f4381cdb7	Temperature Sensor	de0acec2-ea49-49c7-b204-52ba8de44114	1ac136c5-4908-4481-b251-74248670c412
dfe21831-ac99-4c02-80d0-d53f0a6c2113	PH Sensor	9e932134-0683-4947-afaa-3d21f9f6f5ae	aec629d9-df95-48b5-b7d3-ca125e28536c
bcf4a06a-0d78-4169-8e07-b4cc68c82975	TDS Sensor	9e932134-0683-4947-afaa-3d21f9f6f5ae	a99d1069-8e26-40a8-9589-c0fe619f14eb
78837596-074f-4dad-a9aa-343ed69d0852	Temperature Sensor	9e932134-0683-4947-afaa-3d21f9f6f5ae	1ac136c5-4908-4481-b251-74248670c412
449f90b5-a9d7-47d3-a5b0-c89f3d4011f6	PH Sensor	019e43c8-a130-4d83-aa2e-e8b67581d471	aec629d9-df95-48b5-b7d3-ca125e28536c
8d73e8c0-cdb7-4926-8e1a-10155eb9984b	TDS Sensor	019e43c8-a130-4d83-aa2e-e8b67581d471	a99d1069-8e26-40a8-9589-c0fe619f14eb
50c53ee7-9d5a-49e7-8ad1-162053de57fc	Temperature Sensor	019e43c8-a130-4d83-aa2e-e8b67581d471	1ac136c5-4908-4481-b251-74248670c412
255dc460-9e2b-4027-9330-0cde272cd261	PH Sensor	17e59929-2007-4698-adf6-fd9313fb1d7b	aec629d9-df95-48b5-b7d3-ca125e28536c
5e11a401-ee3d-4f34-bbba-93d5ba7972bb	TDS Sensor	17e59929-2007-4698-adf6-fd9313fb1d7b	a99d1069-8e26-40a8-9589-c0fe619f14eb
00f81340-d3f2-4e82-9580-8ad0c2301e80	Temperature Sensor	17e59929-2007-4698-adf6-fd9313fb1d7b	1ac136c5-4908-4481-b251-74248670c412
39518e5c-8ebe-4671-8495-f8f7802dec41	PH Sensor	33ad4e9e-465a-4d5e-a1ad-e4abdf7a61f1	aec629d9-df95-48b5-b7d3-ca125e28536c
46c70bc7-2339-4f87-9961-b72ca3fc5464	TDS Sensor	33ad4e9e-465a-4d5e-a1ad-e4abdf7a61f1	a99d1069-8e26-40a8-9589-c0fe619f14eb
00137b38-2cc0-434f-a885-68eb60fad3b2	Temperature Sensor	33ad4e9e-465a-4d5e-a1ad-e4abdf7a61f1	1ac136c5-4908-4481-b251-74248670c412
6b521ee0-8196-46e6-87b3-5b4ed7301362	PH Sensor	8a67d34f-7f3e-4f5f-a778-ba074147dce6	aec629d9-df95-48b5-b7d3-ca125e28536c
0e87012b-f8cf-4109-bcb4-cdc84103042e	TDS Sensor	8a67d34f-7f3e-4f5f-a778-ba074147dce6	a99d1069-8e26-40a8-9589-c0fe619f14eb
8a1f14bb-10ac-4d12-a98a-c68c1c1b8437	Temperature Sensor	8a67d34f-7f3e-4f5f-a778-ba074147dce6	1ac136c5-4908-4481-b251-74248670c412
ad5ead83-3c17-4aa9-a84f-9ec033aabb7b	PH Sensor	0e54a4d5-72d1-4122-b89d-a91550018531	aec629d9-df95-48b5-b7d3-ca125e28536c
b15a616f-e9a9-4a39-bbe4-19910e507f19	TDS Sensor	0e54a4d5-72d1-4122-b89d-a91550018531	a99d1069-8e26-40a8-9589-c0fe619f14eb
1dfc5bc1-8e23-4e38-87ee-802121e69fb8	Temperature Sensor	0e54a4d5-72d1-4122-b89d-a91550018531	1ac136c5-4908-4481-b251-74248670c412
d6e6534d-5d79-4f00-8bdc-8cca53ab9fa9	PH Sensor	8608fd93-4c24-445e-8fab-c2d6dea1efdc	aec629d9-df95-48b5-b7d3-ca125e28536c
889c3c64-7bc6-4c0a-9563-b4f326e26339	TDS Sensor	8608fd93-4c24-445e-8fab-c2d6dea1efdc	a99d1069-8e26-40a8-9589-c0fe619f14eb
2722c18e-59e7-42cb-af42-62de38ad132d	Temperature Sensor	8608fd93-4c24-445e-8fab-c2d6dea1efdc	1ac136c5-4908-4481-b251-74248670c412
bd7e0fc4-5f27-4e21-9f40-672f9cf1337a	PH Sensor	5f1a842b-fdba-42b1-8b52-9e8aedb6a539	aec629d9-df95-48b5-b7d3-ca125e28536c
f14d0bc7-97e8-4dd4-b061-03cbe364089d	TDS Sensor	5f1a842b-fdba-42b1-8b52-9e8aedb6a539	a99d1069-8e26-40a8-9589-c0fe619f14eb
f4b1bd32-4cc2-4ac4-92b4-46eea9b2ff8a	Temperature Sensor	5f1a842b-fdba-42b1-8b52-9e8aedb6a539	1ac136c5-4908-4481-b251-74248670c412
00faff30-3adb-454a-abd2-04044f7ed8e4	PH Sensor	fbdcc3e6-abcd-4a92-b935-a57023d8a06e	aec629d9-df95-48b5-b7d3-ca125e28536c
90668cf2-e3d3-453c-8512-54b767580f28	TDS Sensor	fbdcc3e6-abcd-4a92-b935-a57023d8a06e	a99d1069-8e26-40a8-9589-c0fe619f14eb
5784c441-c06a-425d-8868-0dccb033edbd	Temperature Sensor	fbdcc3e6-abcd-4a92-b935-a57023d8a06e	1ac136c5-4908-4481-b251-74248670c412
458d8832-6ae2-4907-8a62-99c782a0643b	PH Sensor	f8772530-9cee-406e-8636-89fd73067a1b	aec629d9-df95-48b5-b7d3-ca125e28536c
ffae8e34-cff3-4230-ad86-6a7931531e33	TDS Sensor	f8772530-9cee-406e-8636-89fd73067a1b	a99d1069-8e26-40a8-9589-c0fe619f14eb
11d5d254-2a1d-4446-8b7d-2d3c401622a2	Temperature Sensor	f8772530-9cee-406e-8636-89fd73067a1b	1ac136c5-4908-4481-b251-74248670c412
75ceab8b-5589-45c0-b7ce-4ed3151390de	PH Sensor	d785a778-b919-44ea-8793-d258a0edd6a9	aec629d9-df95-48b5-b7d3-ca125e28536c
fa8fd0d1-3504-42dc-9d09-004979a0b6e5	TDS Sensor	d785a778-b919-44ea-8793-d258a0edd6a9	a99d1069-8e26-40a8-9589-c0fe619f14eb
a61a6fdf-c373-4345-8d46-03b272cb0b1c	Temperature Sensor	d785a778-b919-44ea-8793-d258a0edd6a9	1ac136c5-4908-4481-b251-74248670c412
8d289129-59ca-4e63-9a7c-a6953ad8ff85	PH Sensor	726b0bdd-e014-4d4d-a914-067f2a00161a	aec629d9-df95-48b5-b7d3-ca125e28536c
e81d3f93-08c5-42f1-8bad-dc354afc551a	TDS Sensor	726b0bdd-e014-4d4d-a914-067f2a00161a	a99d1069-8e26-40a8-9589-c0fe619f14eb
a7c69c86-7d6f-4b58-9e24-b5ad489b1460	Temperature Sensor	726b0bdd-e014-4d4d-a914-067f2a00161a	1ac136c5-4908-4481-b251-74248670c412
\.


COPY public."SensorCalibrations" (id, date, calibration_pass, sensor_id) FROM stdin;
1	2024-01-01 00:00:00	t	cc64249d-c2ca-4e1f-8e21-3c628f5302dc
2	2024-01-08 00:00:00	f	cc64249d-c2ca-4e1f-8e21-3c628f5302dc
3	2024-01-15 00:00:00	t	cc64249d-c2ca-4e1f-8e21-3c628f5302dc
4	2024-01-01 00:00:00	t	ff27e3a0-d8e6-44e4-9b77-131db4d23e18
5	2024-01-08 00:00:00	f	ff27e3a0-d8e6-44e4-9b77-131db4d23e18
6	2024-01-15 00:00:00	t	ff27e3a0-d8e6-44e4-9b77-131db4d23e18
7	2024-01-01 00:00:00	t	40611259-0ea7-423b-a768-c2c3bc579104
8	2024-01-08 00:00:00	f	40611259-0ea7-423b-a768-c2c3bc579104
9	2024-01-15 00:00:00	t	40611259-0ea7-423b-a768-c2c3bc579104
\.


COPY public."SensorReadings" (id, date, value, sensor_id) FROM stdin;
1	2024-01-15 00:00:00	7	cc64249d-c2ca-4e1f-8e21-3c628f5302dc
2	2024-01-15 00:10:00	7.1	cc64249d-c2ca-4e1f-8e21-3c628f5302dc
3	2024-01-15 00:20:00	6.8	cc64249d-c2ca-4e1f-8e21-3c628f5302dc
4	2024-01-15 00:00:00	500	ff27e3a0-d8e6-44e4-9b77-131db4d23e18
5	2024-01-15 00:10:00	487.9	ff27e3a0-d8e6-44e4-9b77-131db4d23e18
6	2024-01-15 00:20:00	510.32	ff27e3a0-d8e6-44e4-9b77-131db4d23e18
7	2024-01-15 00:00:00	25	40611259-0ea7-423b-a768-c2c3bc579104
8	2024-01-15 00:10:00	24.2	40611259-0ea7-423b-a768-c2c3bc579104
9	2024-01-15 00:20:00	25.4	40611259-0ea7-423b-a768-c2c3bc579104
\.

