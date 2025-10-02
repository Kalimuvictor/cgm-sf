def get_context(context):
    # Page basic info
    context.title = "CGM Student Fellowship"

    # Top navigation
    context.nav_links_top = [
        {"label": "About Us", "href": "/about"},
        {"label": "Contact", "href": "/contact"}
    ]

    # Main hero content
    context.hero = {
        "heading": "Welcome to CGM Student Fellowship",
        "paragraphs": [
            """The Christ Gospel Messengers Student Fellowship (CGM SF)  ni chombo maalumu cha huduma ya injili
kwa ajili ya vijana wa vyuo vikuu na vyuo vya kati pamoja na vijana wa shule za sekondari,na shule 
za msingi.
CGM SF ni chombo cha kuendeleza na kuimarisha imani ya vijana katika Kristo Yesu, na pia kuwasaidia
vijana katika masuala mbalimbali ya kiroho, kielimu na kijamii. Kwani vijana ni nguzo muhimu katika
jamii na ni matumaini ya taifa.
Kwa kuwa vijana ni nguzo muhimu katika jamii, CGM SF ipo katika kuwasaidia vijana katika masuala
mbalimbali ya kiroho, kielimu na kijamii. Hivyo basi, CGM SF inawasaidia vijana kuwa na imani
thabiti katika Kristo Yesu, na pia kuwasaidia katika masuala mbalimbali ya maisha yao.""" ,
            """Daima CGM SF sera yetu itakua "ELIMU MBELE, WOKOVU MBELE NA KURUDI NYUMA NI MWIKO/MARUFUKU". Kwa Hiyo
kama wanafunzi lazima Elimu iwe kipaumbele kwetu sote, lakini pia wokovu ni kipaumbele muhimu zaidi, 
kwani wokovu ni maisha ya milele, na maisha ya milele ni muhimu zaidi kuliko maisha ya dunia hii. Hivyo 
basi, kama wanafunzi lazima tuwe na elimu na wokovu ili tuweze kuwa watu bora katika jamii yetu.Na kila 
amwaminiye Yesu Kristo kua ni Bwana na mwokozi wake/wa maisha yake ataokoka na kuupata WOKOVU.
Hivyo basi, tunawaalika wanafunzi wote kwanza kabisa kwa wale ambao bado hawajaokoka, mkaribishwa sana
kwa mwaliko mkuu sana wa Bwana Yesu Kristo, kwani kwa sauti yake ya upole anawaita mje kwake na kwa kusema
hivyo kazi yako wewe ni kumkiri Yesu Kristo kuwa Bwana na mwokozi wako, ili uweze kuupata wokovu wa milele.
Na kwa wale ambao tayari mnaokoka, mkaribishwa sana kujiunga nasi katika huduma hii ya CGM SF ili tuweze
kuimarisha imani yetu/zetu katika Kristo Yesu, na pia tuweze kuwasaidia wengine katika masuala mbalimbali ya kiroho,
kielimu na kijamii.""" ,
            """Your gateway to student fellowship, spiritual growth, and academic empowerment.<br>
CGM SF is a place where students come together to nurture their faith, excel academically, and build lifelong friendships."""
        ]
    }

    # CTA Buttons
    context.cta_buttons = [
        {"label": "ELIMU KWANZA", "href": "/about", "color": "#3498db"},
        {"label": "WOKOVU KWANZA", "href": "/contact.html", "color": "#2ecc71"}
    ]

    # Hero background image
    context.hero_bg_image = "/files/image.jpeg"

    # Bottom navigation
    context.nav_links_bottom = [
        {"label": "Jisajili", "href": "/usajili/new"}
    ]
    #footer
    context.footer = {
        "text": "© 2025 CGM Student Fellowship. All rights reserved."
    }
    #header
    context.header = {
        "title": "CGM Student Fellowship",
        "logo": "/files/cgm_logo.png"
    }
