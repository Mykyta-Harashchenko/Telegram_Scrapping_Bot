

## Run Docker Container with pass

```docker run --name mongo_container -e MONGO_INITDB_ROOT_USERNAME=herkules -e MONGO_INITDB_ROOT_PASSWORD=12345 -p 27017:27017 mongo:latest```


## HW
1) Не дублювати в Базі користувачів
2) Якщо юзер заблокував бота - то робити його не активним
3) Функцію get_all_users - зробити щоб відбирала тільки активних юзерів
4) Якщо юзер заблокував бота, але потім розблокував і натиснув /start - то його активувати