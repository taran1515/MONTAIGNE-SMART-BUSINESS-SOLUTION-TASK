Example_list = [{'model': 'auth_api.user', 'pk': 199, 'fields': {'password': 'pbkdf2_sha256$120000$ZWsTOyx6pAdj$o2YzlAyLus5dCXKc6wyYTSQcTFU8oNRP54kwE6lOfys=', 'last_login': None, 'is_superuser': False, 'username': 'price', 'first_name': '', 'last_name': '', 'email': 'prfe@price.com', 'is_staff': False, 'is_active': True, 'date_joined': '2019-05-09T07:00:47.721Z', 'user_type': 'Admin', 'company_name': None, 'phone_num': None, 'Des': None, 'owner': None, 'plan': None, 'groups': [], 'user_permissions': []}},
{'model': 'auth_api.user', 'pk': 200, 'fields': {'password': 'pbkdf2_sha256$120000$ZWsTOyx6pAdj$o2YzlAyLus5dCXKc6wyYTSQcTFU8oNRP54kwE6lOfys=', 'last_login': None, 'is_superuser': False, 'username': 'price', 'first_name': '', 'last_name': '', 'email': 'prfe@price.com', 'is_staff': False, 'is_active': True, 'date_joined': '2019-05-09T07:00:47.721Z', 'user_type': 'Admin', 'company_name': None, 'phone_num': None, 'Des': None, 'owner': None, 'plan': None, 'groups': [], 'user_permissions': []}}, {'model': 'auth_api.user', 'pk': 199, 'fields': {'password': 'pbkdf2_sha256$120000$ZWsTOyx6pAdj$o2YzlAyLus5dCXKc6wyYTSQcTFU8oNRP54kwE6lOfys=', 'last_login': None, 'is_superuser': False, 'username': 'price', 'first_name': '', 'last_name': '', 'email': 'prfe@price.com', 'is_staff': False, 'is_active': True, 'date_joined': '2019-05-09T07:00:47.721Z', 'user_type': 'Admin', 'company_name': None, 'phone_num': None, 'Des': None, 'owner': None, 'plan': None, 'groups': [], 'user_permissions': []}},
{'model': 'auth_api.user', 'pk': 201, 'fields': {'password': 'pbkdf2_sha256$120000$ZWsTOyx6pAdj$o2YzlAyLus5dCXKc6wyYTSQcTFU8oNRP54kwE6lOfys=', 'last_login': None, 'is_superuser': False, 'username': 'price', 'first_name': '', 'last_name': '', 'email': 'prfe@price.com', 'is_staff': False, 'is_active': True, 'date_joined': '2019-05-09T07:00:47.721Z', 'user_type': 'Admin', 'company_name': None, 'phone_num': None, 'Des': None, 'owner': None, 'plan': None, 'groups': [], 'user_permissions': []}}]



print("Original list : " + str(Example_list))


res_list = []
for i in range(len(Example_list)):
    if Example_list[i] not in Example_list[i + 1:]:
        res_list.append(Example_list[i])

print("Resultant list is : " + str(res_list))