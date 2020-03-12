import json

mKB = {
    'one_time': True,
    'buttons':
    [
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"wallet\"}",
                        "label": "Украсть деньги со счета"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"mainMenu\":\"profile\"}",
                        "label": "Получить доступ к профилю"
                    },
                "color": "secondary"
            }
        ]
    ]
}

hCKB = {
        'one_time': True,
        'buttons':
        [
            [
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"name\"}",
                            "label": "Имя"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"work\"}",
                            "label": "Работа"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"color\"}",
                            "label": "Любимый Цвет"
                        },
                    "color": "secondary"
                }                     
            ],
            [
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"eyes\"}",
                            "label": "Цвет Глаз"
                        },
                    "color": "secondary"
                },

                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"hair\"}",
                            "label": "Цвет волос"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"music\"}",
                            "label": "Любимая музыка"
                        },
                    "color": "secondary"
                }                     
            ],
            [
                {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"button\":\"end\"}",
                        "label": "Завершить"
                    },
                "color": "negative"
                },
                
                {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"button\":\"confirm\"}",
                        "label": "Подтвердить"
                    },
                "color": "positive"
                }       
                
            ]
        ]
    }

dKB = {
    'one_time': True,
    'buttons':
    [        
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"district\":\"Фавеллы\"}",
                        "label": "Фавеллы"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"district\":\"Ист-Енд\"}",
                        "label": "Ист-Енд"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"district\":\"Коулун\"}",
                        "label": "Коулун"
                    },
                "color": "secondary"
            }               
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"district\":\"Тобэй\"}",
                        "label": "Тобэй"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"district\":\"Доминго\"}",
                        "label": "Доминго"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"district\":\"Дурбан\"}",
                        "label": "Дурбан"
                    },
                "color": "secondary"
            }               
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"district\":\"Кангване\"}",
                        "label": "Кангване"
                    },
                "color": "secondary"
            } 
        ]
        
    ]
}

heKB = {
    'one_time': True,
    'buttons':
    [
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"height\":\"Низкий\"}",
                        "label": "Низкий"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"height\":\"Средний\"}",
                        "label": "Средний"
                    },
                "color": "secondary"
            }
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"height\":\"Высокий\"}",
                        "label": "Высокий"
                    },
                "color": "secondary"
            }         
        ]
    ]
}

nKB = {
    'one_time': True,
    'buttons':[]
}

wKB = {
    'one_time': True,
    'buttons':
    [        
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"work\":\"shogun\"}",
                        "label": "ShoGun"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"work\":\"sintech\"}",
                        "label": "SinTech"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"work\":\"cybersteel\"}",
                        "label": "CyberSteel"
                    },
                "color": "secondary"
            }               
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"work\":\"c-corp\"}",
                        "label": "C-Corp"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"work\":\"dell\"}",
                        "label": "Dell"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"work\":\"obs news\"}",
                        "label": "OBS News"
                    },
                "color": "secondary"
            }               
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"work\":\"workless\"}",
                        "label": "Безработный"
                    },
                "color": "secondary"
            } 
        ]
        
    ]
}

eKB = {
    'one_time': True,
    'buttons':
    [        
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"eyeColor\":\"зеленые\"}",
                        "label": "Зеленый"
                    },
                "color": "secondary"
            },
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"eyeColor\":\"Синие\"}",
                        "label": "Синий"
                    },
                "color": "secondary"
            }                
        ],
        [
            {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"eyeColor\":\"коричневые\"}",
                        "label": "Карий"
                    },
                "color": "secondary"
            }               
        ]   
    ]
}
hairKB = {
        'one_time': True,
        'buttons':
        [
            [
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"hairColor\":\"Русые\"}",
                            "label": "Русые"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"hairColor\":\"Шатен\"}",
                            "label": "Шатен"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"hairColor\":\"Рыжие\"}",
                            "label": "Рыжие"
                        },
                    "color": "secondary"
                }                     
            ],
            [
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"hairColor\":\"Брюнет\"}",
                            "label": "Брюнет"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"hairColor\":\"Цветные\"}",
                            "label": "Цветные"
                        },
                    "color": "secondary"
                }                     
            ]
        ]
}
hCKB =  {
        'one_time': True,
        'buttons':
        [
            [
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"name\"}",
                            "label": "Имя"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"work\"}",
                            "label": "Работа"
                        },
                    "color": "secondary"
                },
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"district\"}",
                            "label": "Район"
                        },
                    "color": "secondary"
                }                     
            ],
            [
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"eyes\"}",
                            "label": "Цвет Глаз"
                        },
                    "color": "secondary"
                },

                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"hair\"}",
                            "label": "Цвет волос"
                        },
                    "color": "secondary"
                }                  
            ],
            [
                {
                    "action":
                        {
                            "type":"text",
                            "payload": "{\"button\":\"height\"}",
                            "label": "Рост"
                        },
                    "color": "secondary"
                
                }   
            ],
            [
                {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"button\":\"end\"}",
                        "label": "Завершить"
                    },
                "color": "negative"
                },
                
                {
                "action":
                    {
                        "type":"text",
                        "payload": "{\"button\":\"confirm\"}",
                        "label": "Подтвердить"
                    },
                "color": "positive"
                }       
                
            ]
        ]
    }

districtKB = json.dumps(dKB)
nullKB = json.dumps(nKB)
heightKB = json.dumps(heKB)
worksKB = json.dumps(wKB)
hairKB = json.dumps(hairKB)    
humanCreatorKB = json.dumps(hCKB)
eyeColorKB = json.dumps(eKB)


humanCreatorKB = json.dumps(hCKB)
# eyeColorKB = json.dumps(eKB)
mainKB = json.dumps(mKB)