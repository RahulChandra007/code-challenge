# Data was modeled based on Sutterfly sample input for coding and testing
#SimpleLTV for each customer
activity =[
{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d84kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f55c7d8f42", "total_amount": "21.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e805502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "96f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Johnson", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "96f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "10.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "25.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "5.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "255.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f50c7d8f42", "total_amount": "15.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e804002f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "80f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "80f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Williams", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "ac05e804102f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "80f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804202f", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "80f50c7d8f42", "total_amount": "10.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804302f", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "80f50c7d8f42", "total_amount": "25.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804402f", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "80f50c7d8f42", "total_amount": "5.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e804502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "81f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "81f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Jones", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "ac05e804602f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "81f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804702f", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "81f50c7d8f42", "total_amount": "12.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804802f", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "81f50c7d8f42", "total_amount": "28.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "ac05e804902f", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "81f50c7d8f42", "total_amount": "9.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e805506f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "82f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "82f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Brown", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b0d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "82f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a44", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "82f50c7d8f42", "total_amount": "15.04 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a45", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "82f50c7d8f42", "total_amount": "31.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a46", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "82f50c7d8f42", "total_amount": "12.31 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e805507f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "83f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "83f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Davis", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b6d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "83f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a47", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "83f50c7d8f42", "total_amount": "18.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a48", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "83f50c7d8f42", "total_amount": "34.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a49", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "83f50c7d8f42", "total_amount": "15.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e805508f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "84f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "84f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Miller", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b1d91f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "84f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a50", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "84f50c7d8f42", "total_amount": "21.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a51", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "84f50c7d8f42", "total_amount": "37.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a432", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "84f50c7d8f42", "total_amount": "18.55 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e8055202f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "85f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "85f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Wilson", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b1d92f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "85f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d12a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "85f50c7d8f42", "total_amount": "24.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr52k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "85f50c7d8f42", "total_amount": "40.4 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k21a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "85f50c7d8f42", "total_amount": "22.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e2805502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "86f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "86f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Moore", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b31d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "86f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a434", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "86f50c7d8f42", "total_amount": "32.4 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a443", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "86f50c7d8f42", "total_amount": "77.3 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a433", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "86f50c7d8f42", "total_amount": "51.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e8058502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "87f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "87f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Thomas", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b1d98f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "87f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a543", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "87f50c7d8f42", "total_amount": "01.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k14a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "87f50c7d8f42", "total_amount": "215.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k13a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "87f50c7d8f42", "total_amount": "05.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e835502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "88f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "88f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Taylor", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b5d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "88f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d12a4", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "88f50c7d8f42", "total_amount": "1.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5Wk1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "88f50c7d8f42", "total_amount": "215.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k31a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "88f50c7d8f42", "total_amount": "59.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac04e805502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "89f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "89f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Anderson", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede50b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "89f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d5a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "89f50c7d8f42", "total_amount": "1.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a63", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "89f50c7d8f42", "total_amount": "2.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a23", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "89f50c7d8f42", "total_amount": "115.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e825502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "90f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "90f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Jackson", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b3d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "90f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a45", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "90f50c7d8f42", "total_amount": "07.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a63", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "90f50c7d8f42", "total_amount": "66.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a73", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "90f50c7d8f42", "total_amount": "51.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e845502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "91f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "91f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Harris", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b2d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "91f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a45", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "91f50c7d8f42", "total_amount": "4.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a63", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "91f50c7d8f42", "total_amount": "215.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1a73", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "91f50c7d8f42", "total_amount": "15.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e885502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "92f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "92f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Lane", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40b4d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "92f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e8d1a45", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "92f50c7d8f42", "total_amount": "137.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d90kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "92f50c7d8f42", "total_amount": "49.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68g80kr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "92f50c7d8f42", "total_amount": "95.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "cc05e805502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "93f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "93f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Reed", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8sde40b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "93f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80h5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "93f50c7d8f42", "total_amount": "11.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80jr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "93f50c7d8f42", "total_amount": "15.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80lr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "93f50c7d8f42", "total_amount": "15.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "xc05e805502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "94f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "94f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Thompson", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8fde40b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "94f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80g5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "94f50c7d8f42", "total_amount": "1.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80hr5k1a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "94f50c7d8f42", "total_amount": "251.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1z43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "94f50c7d8f42", "total_amount": "51.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e505502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "95f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "95f50c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Martin", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40g1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "95f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1a93", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "95f50c7d8f42", "total_amount": "19.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1s43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "95f50c7d8f42", "total_amount": "21.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k1f43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "95f50c7d8f42", "total_amount": "50.34 USD"},

{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e105502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "99f50c7d8f42", "tags": [{"some key": "some value"}]},
{"type": "CUSTOMER", "verb": "NEW", "key": "99f50c7s8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Chandra", "adr_city": "Middletown", "adr_state": "CA"},
{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede40d1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "99f50c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
{"type": "ORDER", "verb": "NEW", "key": "68d80e5d1f43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "99f50c7d8f42", "total_amount": "17.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k4a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "99f50c7d8f42", "total_amount": "28.34 USD"},
{"type": "ORDER", "verb": "NEW", "key": "68d80kr5k7a43", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "99f50c7d8f42", "total_amount": "95.34 USD"}
]

#The code reads data infile

from datetime import datetime
import operator
import pickle

#Function name : cust_visit
#Input : List structured such as activity
#Calculates : number of site visit made by customer
#Output : Returns a dictionary with customer_id as key and total number of visits as value


def cust_visit(D):
    count_visit = {}
    for act in range(len(D)):
        if "customer_id" in D[act]:
            count_visit[D[act]["customer_id"]] = count_visit.get(D[act]["customer_id"], 1) + 1
    return count_visit

#Function name : cust_period
#Input : customer_id & List structured as activity
#Calculates : number of weeks such that when multiplied by customers total expenditure returns customers weekly expenditure
#Output : returns number of week
def cust_period(cust_id,D):
    time_period =[]
    for act in range(len(D)):
        if "customer_id" in D[act]:
            if (D[act]["customer_id"] == cust_id) or (D[act]["key"] == cust_id):
                time_period.append(D[act]["event_time"])

    #total number of seconds in a week is 7*24*60*60 = 604800
    period = (datetime.strptime(max(time_period), "%Y-%m-%dT%H:%M:%S.%fZ") - datetime.strptime(min(time_period), "%Y-%m-%dT%H:%M:%S.%fZ")).total_seconds()
    # Reversing the number of weeks  to multiply by 52
    # Example if the customer spends $100 in time = 604800*2
    # Then he spends $50 604800 in a week

    if period > 604800: return 604800/period
    else: return 1

#Function Name : tot_cust_expen
#Input : List structured as activity
#Calculates : total expenditure made by each customer
#Output : Returns dictionary with customer_id as key and total expenditure as value
#
def tot_cust_expen(D):
    tot_exp = {}
    for act in range(len(D)):
        if "total_amount" in D[act]:
            if D[act]["customer_id"] not in tot_exp:
                tot_exp[D[act]["customer_id"]] = float(D[act]["total_amount"][:-4])
            else:
                tot_exp[D[act]["customer_id"]] += float(D[act]["total_amount"][:-4])
    return tot_exp

# Simple LTV is defined as 52*a*t
# where a is average customer value per week (customer expenditures per visit (USD) x number of site visits per week)
# t is the life span of the customer
# t for this shutterly - code challenge is 10 years
# 520*a

def TopXSimpleLTVCustomers(x, D):
    #create a sorted list of LTV for all the customers
    #return l[:-x]
    D_Custexp   = tot_cust_expen(D)
    D_Custvisit = cust_visit(D)
    if x > len(D_Custexp): x=len(D_Custexp)
    r={k:float(D_Custvisit[k]*D_Custexp[k]*520) for k in D_Custvisit}
    #dict((key,Custvisit*D_Custexp[key]) for key,Custvisit in D_Custvisit.items())
    for key in r:
        r[key] = round(r[key]*cust_period(key,D),2)# Sort the dictionary by value return a list[(customer_id, simpleLTV)]
    sorted_r = sorted(r.items(),key=operator.itemgetter(1))
    return print(sorted_r[-x:])

def main():
    TopXSimpleLTVCustomers(10, activity)

main()

