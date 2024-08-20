from datetime import datetime, timedelta
from phtml import *
from my_base_html_lib import MyBaseDocument, NavigationContent, SidebarContent, BodyContent, FooterContent

def base_emergency_html_page():
    page_content = Div().add_style({'display': 'block'})

    # # Internet speed
    # fast_internet_div = Div().add_style({'display': 'block', 'margin': '200','padding': '200'})
    # fast_internet_button = Button(
    #     Header(
    #         level=3,
    #         internal='More features if you have good internet'
    #     ).add_style({'margin': '200','padding': '200'})
    # ).add_style({'color': 'white','background-color': 'blue', 'margin': '200','padding': '200'})
    # fast_internet_div.add_element(fast_internet_button)
    # page_content.add_element(fast_internet_div)

    # Scene Size Up
    scene_size_up_div = Div()
    scene_size_up_div.add_element(Header(level=3, internal='Scene Size Up'))
    scene_size_up_list_items = [
        ('"Im Number One"' ,'Look for safety hazards',),
        ('"What Happened to You"' ,'Mechanism of Injury (MOI)',),
        ('"None on Me"' ,'Personal Protective Equipment (PPE)',),
        ('"Are there any more"' ,'Number of Patients',),
        ('"Whats the Vibe"' ,'General assessment of the scene',),
    ]
    scene_size_up_list = HtmlList(ordered=True)
    for item in scene_size_up_list_items:
        row_span = Span().add_style({'display': 'inline'})
        row_span.add_element(Input(type='checkbox'))
        row_span.add_element(Span(item[0]).add_style({'color': 'green'}))
        row_span.add_element(Span(' - '))
        row_span.add_element(Span(item[1]))
        scene_size_up_list.add_element(HtmlListItem(row_span))
    scene_size_up_div.add_element(scene_size_up_list)
    page_content.add_element(scene_size_up_div)

    # Life Threats
    life_threats_div = Div()
    life_threats_div.add_element(Header(level=3, internal='Life Threats'))
    life_threats_list_items = [
        ('A', 'Airway', 'Clear the airway',),
        ('B', 'Breathing', 'Verify they are breathing',),
        ('C', 'Circulation', 'Check for a pulse',),
        ('D', 'Decision on MOI', 'Check for Mechanism of Injury (MOI)',),
        ('E', 'Expose', 'Expose the MOI',),
    ]
    scene_size_up_list = HtmlList(ordered=True)
    for item in life_threats_list_items:
        row_span = Span().add_style({'display': 'inline'})
        row_span.add_element(Input(type='checkbox'))
        row_span.add_element(Span(item[0]).add_style({'color': 'green'}))
        row_span.add_element(Span(' - '))
        row_span.add_element(Span(item[1]).add_style({'color': 'cyan'}))
        row_span.add_element(Span(' - '))
        row_span.add_element(Span(item[2]))
        scene_size_up_list.add_element(HtmlListItem(row_span))
    life_threats_div.add_element(scene_size_up_list)
    page_content.add_element(life_threats_div)

    # Head to Toe
    head_to_toe_div = Div()
    head_to_toe_div.add_element(Header(level=3, internal='Head To Toe Inspection'))
    head_to_toe_list_items = [
        ('Head', 'Check over the head for head trauma'),
        ('Neck', 'Check for neck trauma and alignment'),
        ('Clavicle', 'Check for breaks'),
        ('Shoulders', 'Compress above and below for breaks'),
        ('Ribs', 'Compress sides of ribs for breaks and breathing'),
        ('Stomach Sides', 'Compress sides of stomach for trauma'),
        ('Stomach', 'Find belly button and compress across for trauma'),
        ('Pelvis', 'Compress sides of pelvis for breaks'),
        ('Legs', 'Compress sides of leg muscles for trauma'),
        ('Legs', 'Offset compress of leg for breaks'),
        ('Ankles', 'Compress and check for cracking, popping, or breaks'),
        ('Feet', 'Feel for temperature or swelling to assess circulation'),
        ('Toes', 'Check for feeling in toes by pinching and asking to assess nerve damage'),
        ('Ankles', 'Resist flex, contraction, and rotation of feet'),
        ('Arms', 'Compress sides of arm muscles for trauma'),
        ('Arms', 'Offset compress of arm for breaks'),
        ('Wrists', 'Compress and check for cracking, popping, or breaks'),
        ('Fingers', 'Check for feeling in fingers by pinching and asking to assess nerve damage'),
    ]
    scene_size_up_list = HtmlList(ordered=True)
    for item in head_to_toe_list_items:
        row_span = Span().add_style({'display': 'inline'})
        row_span.add_element(Input(type='checkbox'))
        row_span.add_element(Span(item[0]).add_style({'color': 'green'}))
        row_span.add_element(Span(' - '))
        row_span.add_element(Span(item[1]))
        scene_size_up_list.add_element(HtmlListItem(row_span))
    head_to_toe_div.add_element(scene_size_up_list)
    head_to_toe_div.add_element(Header(level=4, internal='Inspection Notes').add_style({'margin': 10}))
    head_to_toe_div.add_element(Textarea())
    page_content.add_element(head_to_toe_div)

    # Vital Signs
    # History
    # Problem list and Plan
    # Interventions/Treatment
    # Monitor

    navigation_content = NavigationContent(webpage_name="Emergency Info")
    body_content = BodyContent(body_content=[page_content])
    new_formatted_doc = MyBaseDocument(
        navigation_content=navigation_content,
        body_content=body_content,
    )
    return new_formatted_doc.return_document
