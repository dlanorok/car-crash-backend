demo_questionnaire = {
    "car_arrow": "",
    "sections": [
        {
            "id": "starting_questions",
            "name": "Začetna vprašanja",
            "state": "empty",
            "starting_step": "starting_page_initial_page"
        },
        {
            "id": "invite",
            "name": "Povabite",
            "state": "empty",
            "starting_step": "invite"
        },
        {
            "id": "circumstances",
            "name": "Okoliščine",
            "state": "empty",
            "starting_step": "circumstances_initial_page"
        },
        {
            "id": "vehicle_damage",
            "name": "Poškodbe na vozilu",
            "state": "empty",
            "starting_step": "vehicle_damages_initial_page"
        },
        {
            "id": "accident_sketch",
            "name": "Skica nesreče",
            "state": "empty",
            "starting_step": "accident_sketch_initial_page"
        },
        {
            "id": "car_and_insurance",
            "name": "Podatki o zavarovanju in vozilu",
            "state": "empty",
            "starting_step": "car_and_insurance_initial_page"
        },
        {
            "id": "driver",
            "name": "Voznik",
            "state": "empty",
            "starting_step": "driver_initial_page"
        },
        {
            "id": "additional",
            "name": "Dodatno",
            "state": "empty",
            "starting_step": "additional_initial_page"
        },
        {
            "id": "confirmation",
            "name": "Potrditev",
            "state": "empty",
            "starting_step": "confirmation_step_initial_page"
        }
    ],
    "steps": [
        {
            "step_type": "invite",
            "main_screen": True,
            "question": "Soudeleženec naj skenira QR kodo, da lahko povežeta ugotovitve na istem poročilu",
            "help_text": "This is random help text on invite section",
            "inputs": [
                "49"
            ]
        },
        {
            "step_type": "starting_page_initial_page",
            "main_screen": True,
            "chapter": True,
            "question": "BREZ SKRBI, najhuje je za vami. Kar sledi je res enostavno.",
            "help_text": "Začnimo z nekaj enostavnimi, a pomembnimi vprašanji",
            "next_step": "injuries",
            "inputs": [

            ]
        },
        {
            "step_type": "circumstances_initial_page",
            "main_screen": True,
            "chapter": True,
            "question": "OKOLIŠČINE NESREČE",
            "next_step": "circumstances_step_1",
            "inputs": [

            ]
        },
        {
            "step_type": "vehicle_damages_initial_page",
            "main_screen": True,
            "chapter": True,
            "question": "POŠKODBE NA VOZILU",
            "next_step": "collision_direction",
            "inputs": [

            ]
        },
        {
            "step_type": "accident_sketch_initial_page",
            "main_screen": True,
            "chapter": True,
            "question": "SKICA NESREČE",
            "next_step": "accident_sketch",
            "inputs": [

            ]
        },
        {
            "step_type": "car_and_insurance_initial_page",
            "main_screen": True,
            "chapter": True,
            "question": "PODATKI O ZAVAROVANJU",
            "next_step": "car_data",
            "inputs": [

            ]
        },
        {
            "step_type": "driver_initial_page",
            "main_screen": True,
            "chapter": True,
            "question": "PODATKI O VOZNIKU",
            "next_step": "driver_data",
            "inputs": [

            ]
        },
        {
            "step_type": "additional_initial_page",
            "main_screen": True,
            "chapter": True,
            "question": "DODATNE OKOLIŠČINE NESREČE",
            "next_step": "witnesses",
            "inputs": [

            ]
        },
        {
            "step_type": "confirmation_step_initial_page",
            "main_screen": True,
            "chapter": True,
            "question": "POTRDITE POROČILO O PROMETNI NESREČI",
            "next_step": "responsibility_confirmation",
            "inputs": [

            ]
        },
        {
            "step_type": "injuries",
            "question": "Varnost vseh udeleženih je na prvem mestu. Ali je kdo poškodovan (huje ali lažje) in potrebuje medicinsko pomoč? ",
            "help_text": "This is random help text that needs to be changed",
            "next_step": "car_damage",
            "inputs": [
                "1"
            ]
        },
        {
            "step_type": "car_damage",
            "question": "Ali so vidne poškodbe na drugem vozilu?",
            "help_text": "This is random help text on page Damage on other vehicles section",
            "next_step": "property_damage",
            "inputs": [
                "2"
            ]
        },
        {
            "step_type": "property_damage",
            "question": "Ali je kakšna vidna poškodba tudi na drugih objektih (ograje, drevesa,..)",
            "help_text": "This is random help text on page Is there any damage on nearby property",
            "next_step": "accident_place",
            "inputs": [
                "47"
            ]
        },
        {
            "step_type": "accident_place",
            "main_screen": True,
            "question": "Izberite lokacijo",
            "help_text": "This is random help text on Accident place picker",
            "next_step": "accident_time",
            "inputs": [
                "9"
            ]
        },
        {
            "step_type": "accident_time",
            "question": "Datum in ura nesreče",
            "help_text": "This is random help text on Time of accident",
            "next_step": "participants_number",
            "inputs": [
                "7"
            ]
        },
        {
            "step_type": "participants_number",
            "question": "Število udeležencev",
            "help_text": "This is random help text on participant number",
            "inputs": [
                "4"
            ]
        },
        {
            "step_type": "responsibility_confirmation",
            "question": "Kdo je po vaši presoji kriv za nesrečo",
            "help_text": "Help text about responsibility",
            "next_step": "summary_confirmation",
            "inputs": [
                "38"
            ]
        },
        {
            "step_type": "summary_confirmation",
            "question": "Povzetek",
            "next_step": "final_confirmation",
            "main_screen": True,
            "inputs": [
                "51"
            ]
        },
        {
            "step_type": "final_confirmation",
            "question": "Smo na CILJU",
            "help_text": "S klikom na gumb Zaključi potrdite vaše podatke in zaključite postopek. Opozarjamo, da popravljanje poročila po tem koraku ni več možno. Končno Poročilo Vam bomo poslali po elektronski pošti za nadaljno uporabo. Hvala, ker smo vam lahko pomagali v tej neprijetni situacijii!",
            "main_screen": True,
            "inputs": [
                "52"
            ]
        },
        {
            "step_type": "circumstances_step_1",
            "question": "Izberite eno opcijo",
            "help_text": "1",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "3"
            ]
        },
        {
            "step_type": "circumstances_step_2_parked",
            "question": "Izberite eno opcijo",
            "help_text": "2",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "5"
            ]
        },
        {
            "step_type": "circumstances_step_2_moving_parking_joining",
            "question": "Izberite eno opcijo",
            "help_text": "3",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "6"
            ]
        },
        {
            "step_type": "circumstances_step_2_roundabout",
            "question": "Izberite eno opcijo",
            "help_text": "4",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "11"
            ]
        },
        {
            "step_type": "circumstances_step_2_crossing",
            "question": "Izberite eno opcijo",
            "help_text": "5",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "12"
            ]
        },
        {
            "step_type": "circumstances_step_2_straight_road",
            "question": "Izberite eno opcijo",
            "help_text": "6",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "13"
            ]
        },
        {
            "step_type": "circumstances_step_3_parked_leaving_car",
            "question": "Izberite eno opcijo",
            "help_text": "7",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "14"
            ]
        },
        {
            "step_type": "circumstances_step_3_parked_entering_car",
            "question": "Izberite eno opcijo",
            "help_text": "8",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "15"
            ]
        },
        {
            "step_type": "circumstances_step_3_leaving_parking",
            "question": "Izberite eno opcijo",
            "help_text": "9",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "16"
            ]
        },
        {
            "step_type": "circumstances_step_3_parking",
            "question": "Izberite eno opcijo",
            "help_text": "10",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "17"
            ]
        },
        {
            "step_type": "circumstances_step_3_leaving_private_property",
            "question": "Izberite eno opcijo",
            "help_text": "11",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "18"
            ]
        },
        {
            "step_type": "circumstances_step_3_entering_private_property",
            "question": "Izberite eno opcijo",
            "help_text": "12",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "19"
            ]
        },
        {
            "step_type": "circumstances_step_3_roundabout_crashed_another_lane",
            "question": "Izberite eno opcijo",
            "help_text": "13",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "20"
            ]
        },
        {
            "step_type": "circumstances_step_3_roundabout_changing_lanes",
            "question": "Izberite eno opcijo",
            "help_text": "14",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "21"
            ]
        },
        {
            "step_type": "circumstances_step_3_crossing_driving_straight",
            "question": "Izberite eno opcijo",
            "help_text": "15",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "22"
            ]
        },
        {
            "step_type": "circumstances_step_3_crossing_turning_right",
            "question": "Izberite eno opcijo",
            "help_text": "16",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "23"
            ]
        },
        {
            "step_type": "circumstances_step_3_crossing_turning_left",
            "question": "Izberite eno opcijo",
            "help_text": "17",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "24"
            ]
        },
        {
            "step_type": "circumstances_step_3_straight_road_same_direction_another_lane",
            "question": "Izberite eno opcijo",
            "help_text": "18",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "25"
            ]
        },
        {
            "step_type": "circumstances_step_3_straight_road_changing_lanes",
            "question": "Izberite eno opcijo",
            "help_text": "19",
            "updated_inputs": [
                "37"
            ],
            "inputs": [
                "26"
            ]
        },
        {
            "step_type": "collision_direction",
            "main_screen": True,
            "question": "Označite smer naleta",
            "next_step": "damaged_parts",
            "inputs": [
                "27"
            ]
        },
        {
            "step_type": "damaged_parts",
            "main_screen": True,
            "question": "Označite poškodovane dele vozila",
            "inputs": [
                "28"
            ]
        },
        {
            "step_type": "car_data",
            "question": "Vpišite registrsko številko",
            "help_text": "Help ext about registration number",
            "next_step": "insurance_name",
            "inputs": [
                "29",
                "30",
                "40"
            ]
        },
        {
            "step_type": "insurance_name",
            "question": "Izberite vašo zavarovalnico, kjer imate sklenjeno polico za zavarovanje avtomobilske odgovornosti (AO)",
            "help_text": "Help ext about insurance",
            "next_step": "insurance_data",
            "inputs": [
                "31"
            ]
        },
        {
            "step_type": "insurance_data",
            "question": "Vpišite podatke iz vaše police za zavarovanje avtomobilske odgovornosti (AO)",
            "help_text": "Help text about insurance data",
            "next_step": "insurance_holder_data",
            "inputs": [
                "32",
                "41",
                "53",
                "42",
                "50",
                "46"
            ]
        },
        {
            "step_type": "insurance_holder_data",
            "question": "Vpišite podatke o zavarovalcu",
            "help_text": "Help text about insurance holder data",
            "inputs": [
                "43",
                "44",
                "48",
                "45"
            ]
        },
        {
            "step_type": "driver_personal_data",
            "question": "Vpišite vaš email in telefonsko številko, ki se bo uporabila za nadaljno komunikacijo z vami",
            "help_text": "Information about data exchange step",
            "inputs": [
                "33",
                "34"
            ]
        },
        {
            "step_type": "witnesses",
            "question": "Vpišite ime in priimek ter kontaktne podatke vseh prič dogodka",
            "help_text": "Information about witnesses",
            "next_step": "additional_accident_data_text",
            "inputs": [
                "35"
            ]
        },
        {
            "step_type": "driver_data",
            "question": "Poslikajte svoje vozniško dovoljenje za lažji prenos podatkov ali ročno vpišite vaše podatke",
            "help_text": "Help text about scan",
            "next_step": "driver_personal_data",
            "inputs": [
                "36"
            ]
        },
        {
            "step_type": "accident_sketch",
            "main_screen": True,
            "question": "Vizualizacija nesreče",
            "data_from_input": 9,
            "inputs": [
                "37"
            ]
        },
        {
            "step_type": "additional_accident_data_text",
            "question": "Vpišite dodatke okoliščine ali druge pomembne opombe glede nesreče",
            "help_text": "Information about additional data of accident",
            "inputs": [
                "39"
            ]
        },
        {
            "step_type": "case_3_vehicles",
            "question": "3 vehicles not supported",
            "help_text": "This is random help text that needs to be changed 3 vehicles",
            "inputs": [

            ]
        },
        {
            "step_type": "case_1_vehicles",
            "inputs": [

            ],
            "question": "CASCO test",
            "help_text": "This is random help text that needs to be changed"
        }
    ],
    "inputs": {
        "1": {
            "id": 1,
            "type": "select",
            "value": None,
            "required": True,
            "shared_input": True,
            "options": [
                {
                    "value": True,
                    "label": "Pokličite 112",
                    "action": "call",
                    "icon": "car",
                    "action_property": {
                        "number": 112
                    }
                },
                {
                    "value": False,
                    "label": "Nihče ni poškodovan",
                    "icon": "thumbs-up"
                }
            ]
        },
        "37": {
            "id": 37,
            "shared_input": True,
            "type": "sketch",
            "value": {
                "cars": [
                    {
                        "questionnaire_id": 128
                    }
                ],
                "confirmed_editors": [

                ],
                "editing": False
            },
            "required": True
        },
        "2": {
            "id": 2,
            "type": "select",
            "value": None,
            "required": True,
            "shared_input": True,
            "options": [
                {
                    "value": True,
                    "label": "Da",
                    "icon": "car-broken"
                },
                {
                    "value": False,
                    "icon": "car-ok",
                    "label": "Ne"
                }
            ]
        },
        "3": {
            "id": 3,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "parked",
                    "label": "Moje vozilo je bilo parkirano",
                    "action_property": {
                        "step": "circumstances_step_2_parked"
                    }
                },
                {
                    "value": "moving",
                    "label": "Premikal sem vozilo pri parkiranju ali vključevanju v promet",
                    "action_property": {
                        "step": "circumstances_step_2_moving_parking_joining"
                    }
                },
                {
                    "value": "roundabout",
                    "label": "Vozil sem v krožišču",
                    "action_property": {
                        "step": "circumstances_step_2_roundabout"
                    }
                },
                {
                    "value": "crossing",
                    "label": "Vozil sem v križišču",
                    "action_property": {
                        "step": "circumstances_step_2_crossing"
                    }
                },
                {
                    "value": "driving_straight",
                    "label": "Vozil sem po ravni cesti",
                    "action_property": {
                        "step": "circumstances_step_2_straight_road"
                    }
                }
            ]
        },
        "4": {
            "id": 4,
            "type": "select",
            "required": True,
            "value": None,
            "shared_input": True,
            "options": [
                {
                    "value": 1,
                    "label": "1 vozilo",
                    "action_property": {
                        "step": "case_1_vehicles"
                    }
                },
                {
                    "value": 2,
                    "label": "2 vozila"
                },
                {
                    "value": 3,
                    "label": "3 vozila ali več",
                    "action_property": {
                        "step": "case_3_vehicles"
                    }
                }
            ]
        },
        "5": {
            "id": 5,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "leaving_car",
                    "label": "Zapuščal sem parkirano vozilo",
                    "action_property": {
                        "step": "circumstances_step_3_parked_leaving_car"
                    }
                },
                {
                    "value": "entering_parked_car",
                    "label": "Vstopal sem v parkirano vozilo",
                    "action_property": {
                        "step": "circumstances_step_3_parked_entering_car"
                    }
                },
                {
                    "value": "not_in_car",
                    "label": "Ni me bilo ob vozilu"
                }
            ]
        },
        "6": {
            "id": 6,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "leaving_parking_slot",
                    "label": "Zapuščal sem parkirni prostor",
                    "action_property": {
                        "step": "circumstances_step_3_leaving_parking"
                    }
                },
                {
                    "value": "parking",
                    "label": "Zapeljal sem se na parkirni prostor",
                    "action_property": {
                        "step": "circumstances_step_3_parking"
                    }
                },
                {
                    "value": "leaving_parking_slot_private_property",
                    "label": "Zapuščal sem parkirišče, zasebno zemljišče ali poljsko pot",
                    "action_property": {
                        "step": "circumstances_step_3_leaving_private_property"
                    }
                },
                {
                    "value": "entering_parking_slot_private_property",
                    "label": "Zavijal sem na parkirišče, zasebno zemljišče ali poljsko pot",
                    "action_property": {
                        "step": "circumstances_step_3_entering_private_property"
                    }
                }
            ]
        },
        "7": {
            "id": 7,
            "type": "datetime",
            "value": None,
            "required": True,
            "shared_input": True
        },
        "9": {
            "id": 9,
            "type": "place",
            "value": None,
            "required": True,
            "shared_input": True
        },
        "11": {
            "id": 11,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "roundabout_entering",
                    "label": "Vključeval sem se v krožišče"
                },
                {
                    "value": "roundabout_run_into_vehicle",
                    "label": "Naletel sem na vozilo, ki je vozilo pred mano"
                },
                {
                    "value": "roundabout_another_vehicle_crashed_from_behind",
                    "label": "Drugo vozilo se je od zadaj zaletelo vame"
                },
                {
                    "value": "roundabout_crashed_with_vehicle_from_another_traffic_lane",
                    "label": "Trčil sem z vozilom, ki je v krožišču vozilo po drugem voznem pasu",
                    "action_property": {
                        "step": "circumstances_step_3_roundabout_crashed_another_lane"
                    }
                },
                {
                    "value": "roundabout_changing_traffic_lane",
                    "label": "Menjaval sem prometni pas",
                    "action_property": {
                        "step": "circumstances_step_3_roundabout_changing_lanes"
                    }
                }
            ]
        },
        "12": {
            "id": 12,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "crossing_standing_or_traffic_light",
                    "label": "Stal sem pred vključevanjem v promet oziroma pred semaforjem"
                },
                {
                    "value": "crossing_driving_straight",
                    "label": "Vozil sem naravnost čez križišče",
                    "action_property": {
                        "step": "circumstances_step_3_crossing_driving_straight"
                    }
                },
                {
                    "value": "crossing_turning_right",
                    "label": "Zavijal sem desno",
                    "action_property": {
                        "step": "circumstances_step_3_crossing_turning_right"
                    }
                },
                {
                    "value": "crossing_turning_left",
                    "label": "Zavijal sem levo",
                    "action_property": {
                        "step": "circumstances_step_3_crossing_turning_left"
                    }
                }
            ]
        },
        "13": {
            "id": 13,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "driving_straight_crashed_with_vehicle_in_front",
                    "label": "Naletel sem na vozilo, ki je vozilo pred mano"
                },
                {
                    "value": "driving_straight_crashed_from_behind",
                    "label": "Drugo vozilo se je od zadaj zaletelo vame"
                },
                {
                    "value": "driving_straight_crashed_to_vehicle_in_another_lane",
                    "label": "Trčil sem z vozilom, ki je vozilo v isto smer, a v drugem voznem pasu",
                    "action_property": {
                        "step": "circumstances_step_3_straight_road_same_direction_another_lane"
                    }
                },
                {
                    "value": "driving_straight_changing_lane",
                    "label": "Menjaval sem vozni pas",
                    "action_property": {
                        "step": "circumstances_step_3_straight_road_changing_lanes"
                    }
                },
                {
                    "value": "driving_straight_overtaking_another_vehicle",
                    "label": "Prehiteval sem drugo vozilo"
                },
                {
                    "value": "driving_reverse",
                    "label": "Vozil sem vzvratno"
                },
                {
                    "value": "driving_straight_in_opposite_lane",
                    "label": "Vozil sem po voznem pasu za nasprotni promet"
                }
            ]
        },
        "14": {
            "id": 14,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "parked_leaving_car_doors_closed",
                    "label": "Vrata vozila so bila zaprta"
                },
                {
                    "value": "parked_leaving_car_doors_opened",
                    "label": "Vrata vozila so bila zaprta"
                }
            ]
        },
        "15": {
            "id": 15,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "parked_entering_car_doors_closed",
                    "label": "Vrata vozila so bila zaprta"
                },
                {
                    "value": "parked_entering_car_doors_opened",
                    "label": "Vrata vozila so bila zaprta"
                }
            ]
        },
        "16": {
            "id": 16,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "driving_straight",
                    "label": "Vozil sem naravnost"
                },
                {
                    "value": "driving_reverse",
                    "label": "Vozil sem vzvratno"
                }
            ]
        },
        "17": {
            "id": 17,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "driving_straight",
                    "label": "Vozil sem naravnost"
                },
                {
                    "value": "driving_reverse",
                    "label": "Vozil sem vzvratno"
                }
            ]
        },
        "18": {
            "id": 18,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "driving_straight",
                    "label": "Vozil sem naravnost"
                },
                {
                    "value": "driving_reverse",
                    "label": "Vozil sem vzvratno"
                },
                {
                    "value": "turning_left",
                    "label": "Zavijal sem levo"
                },
                {
                    "value": "turning_right",
                    "label": "Zavijal sem desno"
                }
            ]
        },
        "19": {
            "id": 19,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "driving_straight",
                    "label": "Vozil sem naravnost"
                },
                {
                    "value": "driving_reverse",
                    "label": "Vozil sem vzvratno"
                },
                {
                    "value": "turning_left",
                    "label": "Zavijal sem levo"
                },
                {
                    "value": "turning_right",
                    "label": "Zavijal sem desno"
                }
            ]
        },
        "20": {
            "id": 20,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "vehicle_on_right",
                    "label": "Drugo vozilo je bilo na desni strani"
                },
                {
                    "value": "vehicle_on_left",
                    "label": "Drugo vozilo je bilo na levi strani"
                }
            ]
        },
        "21": {
            "id": 21,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "changing_driving_lane_right",
                    "label": "Zapeljal sem na desni vozni pas"
                },
                {
                    "value": "changing_driving_lane_left",
                    "label": "Zapeljal sem na levi vozni pas"
                }
            ]
        },
        "22": {
            "id": 22,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "crossing_entering_from_right",
                    "label": "V križišče sem prihajal s desne glede na drugo vozilo"
                },
                {
                    "value": "crossing_not_obeying_rules",
                    "label": "Nisem upošteval znakov prednosti ali rdeče luči na semaforju"
                }
            ]
        },
        "23": {
            "id": 23,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "crossing_entering_from_right",
                    "label": "V križišče sem prihajal s desne glede na drugo vozilo"
                },
                {
                    "value": "crossing_not_obeying_rules",
                    "label": "Nisem upošteval znakov prednosti ali rdeče luči na semaforju"
                }
            ]
        },
        "24": {
            "id": 24,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "crossing_entering_from_right",
                    "label": "V križišče sem prihajal s desne glede na drugo vozilo"
                },
                {
                    "value": "crossing_not_obeying_rules",
                    "label": "Nisem upošteval znakov prednosti ali rdeče luči na semaforju"
                }
            ]
        },
        "25": {
            "id": 25,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "vehicle_on_right",
                    "label": "Drugo vozilo je bilo na desni strani"
                },
                {
                    "value": "vehicle_on_left",
                    "label": "Drugo vozilo je bilo na levi strani"
                }
            ]
        },
        "26": {
            "id": 26,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "changing_driving_lane_right",
                    "label": "Zapeljal sem na desni vozni pas"
                },
                {
                    "value": "changing_driving_lane_left",
                    "label": "Zapeljal sem na levi vozni pas"
                }
            ]
        },
        "27": {
            "id": 27,
            "type": "collision_direction",
            "value": None,
            "required": True
        },
        "28": {
            "id": 28,
            "type": "damaged_parts",
            "value": None,
            "required": True
        },
        "29": {
            "id": 29,
            "type": "text",
            "on_change_action": "capitalize",
            "label": "Registrska številka",
            "value": "KP RU-408",
            "required": True
        },
        "30": {
            "id": 30,
            "label": "Država",
            "type": "country_picker",
            "value": "SI",
            "required": True
        },
        "31": {
            "id": 31,
            "type": "select",
            "options": [
                {
                    "value": "1",
                    "label": "Generali zavarovalnica d.d."
                },
                {
                    "value": "2",
                    "label": "Grawe zavarovalnica d.d."
                },
                {
                    "value": "3",
                    "label": "Zavarovalnica Sava d.d."
                },
                {
                    "value": "4",
                    "label": "Zavarovalnica Triglav d.d."
                }
            ],
            "value": "4",
            "required": True
        },
        "32": {
            "id": 32,
            "type": "text",
            "label": "Številka zavarovalne police",
            "value": "041669225",
            "required": True
        },
        "33": {
            "id": 33,
            "type": "text",
            "label": "Email naslov",
            "input_type": "email",
            "value": None,
            "required": True
        },
        "34": {
            "id": 34,
            "type": "phone_picker",
            "label": "Telefonska številka",
            "value": None,
            "required": True
        },
        "35": {
            "id": 35,
            "type": "textarea",
            "label": "Priče dogodka",
            "value": None
        },
        "36": {
            "id": 36,
            "type": "driving_license",
            "value": None,
            "required": True
        },
        "38": {
            "id": 38,
            "type": "select",
            "value": None,
            "required": True,
            "options": [
                {
                    "value": "ME",
                    "label": "Jaz"
                },
                {
                    "value": "ANOTHER",
                    "label": "Drugo vozilo"
                },
                {
                    "value": "UNKNOWN",
                    "label": "Ne vem"
                }
            ]
        },
        "39": {
            "id": 39,
            "type": "textarea",
            "label": "Dodatne okoliščine ali druge opombe",
            "value": None
        },
        "40": {
            "id": 40,
            "type": "text",
            "label": "Znamka in tip vozila",
            "value": "Audi A6",
            "required": True
        },
        "41": {
            "id": 41,
            "type": "text",
            "label": "Številka zelene karte",
            "value": "041669225"
        },
        "42": {
            "id": 42,
            "type": "date",
            "label": "Veljavnost do",
            "value": "2024-06-21T10:00:00.000Z",
            "required": True
        },
        "43": {
            "id": 43,
            "type": "text",
            "label": "Zavarovalec",
            "value": "Dario Madžarević",
            "required": True
        },
        "44": {
            "id": 44,
            "type": "text",
            "label": "Naslov zavarovalca",
            "value": "Nazorjeva 2, 6310 Izola",
            "required": True
        },
        "45": {
            "id": 45,
            "label": "Telefonska številka zavarovalca",
            "type": "phone_picker",
            "value": {
                "number": "41 669 225",
                "internationalNumber": "+386 41 669 225",
                "nationalNumber": "041 669 225",
                "e164Number": "+38641669225",
                "countryCode": "SI",
                "dialCode": "+386"
            },
            "required": True
        },
        "46": {
            "id": 46,
            "type": "country_picker",
            "label": "Država zavarovalca",
            "value": "SI",
            "required": True
        },
        "47": {
            "id": 47,
            "type": "select",
            "value": None,
            "required": True,
            "shared_input": True,
            "options": [
                {
                    "value": True,
                    "icon": "crash",
                    "label": "Da"
                },
                {
                    "value": False,
                    "icon": "fill-rect",
                    "label": "Ne"
                }
            ]
        },
        "48": {
            "id": 48,
            "type": "text",
            "input_type": "email",
            "label": "Email zavarovalca",
            "value": "dario.madzarevic@siol.net",
            "required": True
        },
        "49": {
            "id": 49,
            "type": "invite",
            "value": None
        },
        "50": {
            "id": 50,
            "type": "boolean",
            "label": "Ali je vozilo zavarovano tudi kasko?",
            "required": True,
            "value": True
        },
        "51": {
            "id": 51,
            "type": "confirmation",
            "required": True,
            "value": None
        },
        "52": {
            "id": 52,
            "type": "final_step",
            "required": True,
            "value": None
        },
        "53": {
            "id": 53,
            "type": "date",
            "label": "Validity from",
            "value": "2023-06-21T10:00:00.000Z"
        }
    }
}
