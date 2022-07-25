from datetime import datetime

comment1 = {
    "Text": "Hey You",
    "Name": "Dennis",
    "Username": "dennis",
    "Picture": "Black-Dog-PNG.png",
    "Datetime": datetime(2022, 7, 20, 10, 31)
}

comment2 = {
    "Text": "Hey Dennis",
    "Name": "KorKor",
    "Username": "korkor",
    "Picture": "Black-Dog-PNG.png",
    "Datetime": datetime(2022, 7, 21, 20, 31)
}


comment3 = {
    "Text": "Hey Dennis",
    "Name": "KorKor",
    "Username": "korkor",
    "Picture": "Black-Dog-PNG.png",
    "Datetime": datetime(2022, 7, 21, 20, 31)
}
post1 = {
    "PostId" : 1,
    "Name": "KorKor",
    "Text": "Hello King",
    "Username": "korkor",
    "Picture": "Black-Dog-PNG.png",
    "Likes": ["dennis"],
    "Comments":[comment1,comment2 ],
    "Datetime": datetime(2022, 7, 18, 10, 31)
}

post2 = {
    "PostId" : 2,
    "Name": "Dennis",
    "Text": "Take me home",
    "Username": "dennis",
    "Picture": "Black-Dog-PNG.png",
    "Likes": [],
    "Comments":[],
    "Datetime": datetime(2022, 7, 17, 8, 31)
}

post3 = {
    "PostId" : 3,
    "Name": "Gift",
    "Text": "Call me Gift",
    "Username": "gift",
    "Picture": "Black-Dog-PNG.png",
    "Likes": [],
    "Comments":[comment3],
    "Datetime": datetime(2022, 7, 13, 7, 31)
}


test_posts = {
    1 : post1,
    2 : post2,
    3 : post3

}

Korkor_posts = {
    1: post1

}

Gift_posts = {
    3: post3
    
}

Dennis_posts = {
    2: post2
    
}


korkor = {
    "Name": "Korkor",
    "Bio" : "My name is Korkor.  I love food and sleeping.",
    "Username" : "korkor",
    "Picture" : "Black-Dog-PNG.png",
    "Birthday" : datetime(2013, 2, 14),
    "Posts": Korkor_posts
}

gift = {
    "Name": "Gift",
    "Bio" : "My name is Gift. I'm antisocial and I love soup.",
    "Username" : "gift",
    "Picture" : "Black-Dog-PNG.png",
    "Birthday" : datetime(2013, 2, 14),
    "Posts": Gift_posts
}
dennis = {
    "Name": "Dennis",
    "Bio" : "My name is Dennis.  I love to learn new skills.",
    "Username" : "dennis",
    "Picture" : "Black-Dog-PNG.png",
    "Birthday" : datetime(2013, 2, 14),
    "Posts": Dennis_posts
}
dogs= {
    "korkor" : korkor,
    "gift" : gift,
    "dennis" : dennis

}