"""Tourist information data for various cities with ancient heritage sites"""

TOURIST_DATA = [
    # Rome, Italy
    {
        "city": "Rome",
        "country": "Italy",
        "description": "Rome, the Eternal City, is a living museum of ancient Roman civilization. Walking through Rome is like traveling through time, where every corner reveals millennia of history.",
        "heritage_sites": [
            {
                "name": "Colosseum",
                "description": "The iconic amphitheater built in 80 AD, where gladiators once fought. This massive structure could hold 50,000 spectators and remains the largest amphitheater ever built. Marvel at the underground chambers where gladiators prepared for battle.",
                "best_time": "Early morning to avoid crowds",
                "tips": "Book skip-the-line tickets in advance. Visit the underground chambers for a unique perspective."
            },
            {
                "name": "Roman Forum",
                "description": "The heart of ancient Rome, where politics, commerce, and daily life unfolded. Walk among the ruins of temples, basilicas, and government buildings that once formed the center of the Roman Empire.",
                "best_time": "Late afternoon for beautiful lighting",
                "tips": "Combine with Palatine Hill ticket. Wear comfortable shoes as you'll be walking on ancient stones."
            },
            {
                "name": "Pantheon",
                "description": "A remarkably preserved Roman temple built in 126 AD, featuring the world's largest unreinforced concrete dome. The oculus at the top is the only source of natural light, creating a mystical atmosphere.",
                "best_time": "Midday when sunlight streams through the oculus",
                "tips": "Entry is free but expect queues. Visit the tombs of Italian kings and Raphael inside."
            }
        ],
        "local_tips": "Try authentic Roman cuisine like carbonara and cacio e pepe. The city is best explored on foot.",
        "best_season": "Spring (April-May) or Fall (September-October)"
    },

    # Athens, Greece
    {
        "city": "Athens",
        "country": "Greece",
        "description": "Athens, the birthplace of democracy and Western civilization, offers an unparalleled journey through ancient Greek history. The city where philosophy, drama, and democracy were born.",
        "heritage_sites": [
            {
                "name": "Acropolis and Parthenon",
                "description": "The crown jewel of ancient Greece, perched on a rocky outcrop overlooking Athens. The Parthenon, dedicated to goddess Athena, is a masterpiece of classical architecture dating to 447 BC.",
                "best_time": "First thing in the morning or sunset",
                "tips": "Buy combo tickets for all archaeological sites. Wear non-slip shoes as marble can be slippery."
            },
            {
                "name": "Ancient Agora",
                "description": "The heart of ancient Athenian life, where Socrates taught and democracy was practiced. Explore the well-preserved Temple of Hephaestus and the reconstructed Stoa of Attalos.",
                "best_time": "Morning hours",
                "tips": "The museum in the Stoa of Attalos provides excellent context for the site."
            },
            {
                "name": "Temple of Olympian Zeus",
                "description": "Once one of the largest temples in the ancient world, construction spanned over 700 years. Only 15 of the original 104 colossal columns remain standing, each 17 meters high.",
                "best_time": "Late afternoon",
                "tips": "Best viewed in combination with Hadrian's Arch nearby."
            }
        ],
        "local_tips": "Explore the Plaka neighborhood for traditional tavernas. Try souvlaki and Greek salad at local eateries.",
        "best_season": "Spring (April-June) or Fall (September-October)"
    },

    # Cairo, Egypt
    {
        "city": "Cairo",
        "country": "Egypt",
        "description": "Cairo, the gateway to ancient Egyptian civilization, offers an incomparable journey to one of humanity's greatest ancient civilizations. Home to the only surviving Wonder of the Ancient World.",
        "heritage_sites": [
            {
                "name": "Pyramids of Giza",
                "description": "The last remaining Wonder of the Ancient World, built around 2560 BC. The Great Pyramid of Khufu, along with the pyramids of Khafre and Menkaure, and the enigmatic Sphinx, represent the pinnacle of ancient Egyptian engineering.",
                "best_time": "Early morning or late afternoon to avoid heat and crowds",
                "tips": "Hire a licensed guide for historical context. You can enter some pyramids for an additional fee. Camel rides are available but negotiate prices beforehand."
            },
            {
                "name": "Egyptian Museum",
                "description": "Houses the world's largest collection of ancient Egyptian artifacts, including the treasures of Tutankhamun. Over 120,000 items spanning 5,000 years of history.",
                "best_time": "Opening time or late afternoon",
                "tips": "Allow at least 3-4 hours. The Tutankhamun galleries are a must-see."
            },
            {
                "name": "Saqqara",
                "description": "Home to the Step Pyramid of Djoser, the oldest stone pyramid in Egypt (2650 BC). Less crowded than Giza but equally fascinating, with multiple pyramids and tombs with original hieroglyphics.",
                "best_time": "Morning",
                "tips": "Combine with Memphis. The site is vast, so wear comfortable shoes."
            }
        ],
        "local_tips": "Try traditional Egyptian dishes like koshari and ful medames. Bargain in markets but be respectful.",
        "best_season": "Winter (November-February) for comfortable temperatures"
    },

    # Istanbul, Turkey
    {
        "city": "Istanbul",
        "country": "Turkey",
        "description": "Istanbul, the bridge between East and West, served as capital of three great empires: Roman, Byzantine, and Ottoman. This magnificent city straddles two continents and millennia of history.",
        "heritage_sites": [
            {
                "name": "Hagia Sophia",
                "description": "A architectural marvel built in 537 AD as a Byzantine cathedral, later converted to a mosque, then a museum, and now a mosque again. Its massive dome and golden mosaics represent Byzantine artistry at its peak.",
                "best_time": "Early morning to avoid crowds",
                "tips": "Dress modestly. Women should bring a headscarf. Free entry but expect security queues."
            },
            {
                "name": "Blue Mosque",
                "description": "The Sultan Ahmed Mosque, built in 1616, is famous for its six minarets and stunning blue Iznik tiles adorning the interior. A masterpiece of Ottoman architecture.",
                "best_time": "Outside prayer times",
                "tips": "Entry is free. Remove shoes before entering. Dress modestly."
            },
            {
                "name": "Topkapi Palace",
                "description": "The primary residence of Ottoman sultans for 400 years. Explore opulent courtyards, the Imperial Treasury with jewels, the sacred relics chamber, and the Harem.",
                "best_time": "Opening time",
                "tips": "Buy tickets online. The Harem requires a separate ticket but is worth it."
            }
        ],
        "local_tips": "Take a Bosphorus cruise to see the city from water. Try Turkish breakfast, kebabs, and baklava.",
        "best_season": "Spring (April-May) or Fall (September-October)"
    },

    # Kyoto, Japan
    {
        "city": "Kyoto",
        "country": "Japan",
        "description": "Kyoto, Japan's ancient capital for over 1,000 years, is the heart of traditional Japanese culture. With 17 UNESCO World Heritage sites, it offers an unmatched journey through Japanese history.",
        "heritage_sites": [
            {
                "name": "Fushimi Inari Shrine",
                "description": "Famous for its thousands of vermillion torii gates forming tunnels up the sacred Mount Inari. Dating to 711 AD, this Shinto shrine dedicated to the rice god is one of Japan's most iconic sites.",
                "best_time": "Early morning or late afternoon",
                "tips": "Free entry. The full hike takes 2-3 hours but you can turn back anytime. Bring water."
            },
            {
                "name": "Kinkaku-ji (Golden Pavilion)",
                "description": "A Zen Buddhist temple covered in gold leaf, perfectly reflected in the pond below. Originally built in 1397 as a retirement villa, it's one of Kyoto's most photographed sites.",
                "best_time": "Early morning for best light and fewer crowds",
                "tips": "No interior access but the gardens are beautiful. Best in autumn colors or with snow."
            },
            {
                "name": "Kiyomizu-dera Temple",
                "description": "A historic Buddhist temple founded in 778 AD, famous for its wooden stage jutting out from the main hall, 13 meters above the hillside. Offers stunning views of Kyoto.",
                "best_time": "Early morning or evening",
                "tips": "The surrounding Higashiyama district is perfect for exploring traditional streets."
            }
        ],
        "local_tips": "Experience a traditional tea ceremony. Rent a kimono for a day. Visit the Arashiyama Bamboo Grove.",
        "best_season": "Spring (cherry blossoms) or Fall (autumn foliage)"
    },

    # Machu Picchu, Peru
    {
        "city": "Cusco",
        "country": "Peru",
        "description": "Cusco, the ancient capital of the Inca Empire, serves as the gateway to Machu Picchu. The city itself is a UNESCO World Heritage site, blending Incan and Spanish colonial architecture.",
        "heritage_sites": [
            {
                "name": "Machu Picchu",
                "description": "The Lost City of the Incas, built in the 15th century and abandoned during the Spanish conquest. This breathtaking citadel sits 2,430 meters above sea level, surrounded by cloud forest. One of the New Seven Wonders of the World.",
                "best_time": "Early morning for fewer crowds and possible cloud lifting",
                "tips": "Book tickets and train months in advance. Consider hiking the Inca Trail or taking the train. Acclimatize in Cusco first to avoid altitude sickness."
            },
            {
                "name": "Sacsayhuamán",
                "description": "Massive Incan fortress overlooking Cusco, built with precisely cut stones weighing up to 200 tons. The engineering marvel of how these stones were moved and fitted without mortar remains a mystery.",
                "best_time": "Afternoon",
                "tips": "Combine with other nearby ruins using the Boleto Turístico ticket."
            },
            {
                "name": "Qorikancha (Temple of the Sun)",
                "description": "The most important temple in the Inca Empire, once covered in gold. The Spanish built Santo Domingo Convent on top, creating a unique blend of Incan and colonial architecture.",
                "best_time": "Morning",
                "tips": "The museum provides excellent context about Incan astronomy and architecture."
            }
        ],
        "local_tips": "Try ceviche, lomo saltado, and coca tea for altitude. Spend 2-3 days in Cusco to acclimatize before Machu Picchu.",
        "best_season": "May to September (dry season)"
    },

    # Jerusalem, Israel
    {
        "city": "Jerusalem",
        "country": "Israel",
        "description": "Jerusalem, one of the world's oldest cities, is sacred to Judaism, Christianity, and Islam. With over 3,000 years of history, it's a spiritual epicenter where ancient and modern worlds collide.",
        "heritage_sites": [
            {
                "name": "Old City of Jerusalem",
                "description": "Divided into four quarters (Jewish, Christian, Muslim, Armenian), this ancient walled city contains sites holy to multiple religions. Walk through narrow stone streets that have witnessed millennia of history.",
                "best_time": "Early morning in each quarter",
                "tips": "Wear modest clothing. The city closes early on Friday for Shabbat."
            },
            {
                "name": "Western Wall",
                "description": "The holiest site in Judaism, this retaining wall of the Second Temple complex dates to 19 BC. Millions come here annually to pray and place written prayers in the wall's cracks.",
                "best_time": "Friday evening for Shabbat prayers",
                "tips": "Dress modestly. Men should cover their heads. The plaza is divided into men's and women's sections."
            },
            {
                "name": "Church of the Holy Sepulchre",
                "description": "Built on the site where Jesus is believed to have been crucified and buried. This 4th-century church is Christianity's holiest site, shared by multiple Christian denominations.",
                "best_time": "Early morning",
                "tips": "Free entry but expect crowds. Respectful behavior required."
            }
        ],
        "local_tips": "Try falafel, hummus, and shakshuka. Navigate between quarters to experience different cultures. Be aware of religious holidays and closures.",
        "best_season": "Spring (March-May) or Fall (September-November)"
    },

    # Angkor Wat, Cambodia
    {
        "city": "Siem Reap",
        "country": "Cambodia",
        "description": "Siem Reap is the gateway to Angkor Archaeological Park, containing the magnificent remains of the Khmer Empire. These temples represent the pinnacle of Southeast Asian architecture.",
        "heritage_sites": [
            {
                "name": "Angkor Wat",
                "description": "The largest religious monument in the world, built in the 12th century as a Hindu temple dedicated to Vishnu, later converted to Buddhism. This architectural masterpiece represents Mount Meru, home of the gods in Hindu mythology.",
                "best_time": "Sunrise is magical, but very crowded. Late afternoon is also beautiful.",
                "tips": "Multi-day pass recommended. Dress modestly for temples. Hire a guide for historical context."
            },
            {
                "name": "Bayon Temple",
                "description": "Famous for its 216 serene stone faces carved into massive towers. Built in the late 12th century, this Buddhist temple at the center of Angkor Thom creates an mystical atmosphere.",
                "best_time": "Mid-morning for best light on the faces",
                "tips": "Combine with other Angkor Thom temples. The faces are best photographed with side lighting."
            },
            {
                "name": "Ta Prohm",
                "description": "The jungle temple where massive tree roots engulf ancient stones. Left largely unrestored to maintain its mysterious, atmospheric quality. Made famous by the Tomb Raider movie.",
                "best_time": "Early morning or late afternoon",
                "tips": "Very popular, so arrive early or late. The combination of architecture and nature is unique."
            }
        ],
        "local_tips": "Try Khmer cuisine including fish amok and lok lak. Tuk-tuks are the main transport. Stay hydrated in the heat.",
        "best_season": "November to February (cool and dry)"
    },

    # Petra, Jordan
    {
        "city": "Petra",
        "country": "Jordan",
        "description": "Petra, the Rose City, is an archaeological wonder carved directly into vibrant red sandstone cliffs by the Nabataeans over 2,000 years ago. This ancient trading city is one of the New Seven Wonders of the World.",
        "heritage_sites": [
            {
                "name": "The Treasury (Al-Khazneh)",
                "description": "Petra's most iconic monument, carved from sandstone around 100 AD. This 40-meter-high facade glows in shades of pink and red. Reached through the dramatic Siq, a narrow gorge over 1 kilometer long.",
                "best_time": "Early morning when sunlight first hits the facade, or late afternoon",
                "tips": "Walk through the Siq slowly to appreciate the ancient engineering. The Treasury is just the beginning of Petra."
            },
            {
                "name": "The Monastery (Ad Deir)",
                "description": "Larger than the Treasury but less crowded. Requires climbing 800 rock-cut steps, but the views and the massive 50-meter facade are worth it. Built in the 3rd century BC.",
                "best_time": "Late afternoon for stunning light",
                "tips": "Bring water and wear good shoes. The climb takes 30-40 minutes. Viewpoints above offer spectacular vistas."
            },
            {
                "name": "Royal Tombs",
                "description": "A series of impressive facades carved into the cliff face, including the Urn Tomb, Silk Tomb, and Corinthian Tomb. These served as elaborate burial chambers for Nabataean royalty.",
                "best_time": "Afternoon when the sun illuminates the facades",
                "tips": "You can climb inside some tombs. The views from the Urn Tomb are excellent."
            }
        ],
        "local_tips": "Wear sturdy hiking shoes and sun protection. Bring plenty of water. Consider a multi-day pass to fully explore. Try traditional Jordanian mansaf.",
        "best_season": "Spring (March-May) or Fall (September-November)"
    },

    # Delhi, India
    {
        "city": "Delhi",
        "country": "India",
        "description": "Delhi, India's capital, has been continuously inhabited for over 2,500 years and served as the capital of numerous empires. The city is a treasure trove of monuments spanning multiple centuries and dynasties.",
        "heritage_sites": [
            {
                "name": "Red Fort",
                "description": "A massive red sandstone fort built by Mughal Emperor Shah Jahan in 1648. This UNESCO World Heritage site served as the main residence of Mughal emperors for nearly 200 years. Its walls span 2.5 kilometers.",
                "best_time": "Early morning or late afternoon",
                "tips": "The light and sound show in the evening is worth attending. Allow 2-3 hours to explore."
            },
            {
                "name": "Qutub Minar",
                "description": "A 73-meter tall minaret built in 1193, the world's tallest brick minaret. This UNESCO World Heritage site showcases Indo-Islamic architecture and features intricate carvings and verses from the Quran.",
                "best_time": "Morning or late afternoon",
                "tips": "Explore the entire Qutub complex including the Iron Pillar that hasn't rusted in 1,600 years."
            },
            {
                "name": "Humayun's Tomb",
                "description": "Built in 1570, this magnificent garden tomb was the inspiration for the Taj Mahal. The first garden-tomb on the Indian subcontinent, it represents Mughal architecture at its finest.",
                "best_time": "Late afternoon for beautiful lighting",
                "tips": "The gardens are perfect for a leisurely stroll. Combine with nearby Nizamuddin Dargah."
            }
        ],
        "local_tips": "Try street food at Chandni Chowk. Use metro for easy navigation. Visit Jama Masjid, India's largest mosque. Dress modestly at religious sites.",
        "best_season": "October to March (pleasant weather)"
    }
]
