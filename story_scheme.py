title_pic_dir = ""
save_name = ""
title_pic_color = 0
menu_color = 0
list_ps = [ ]

def check(story: dict):

    # check to see if title tag is in scene 0 + initialization
    if 'title' in story['adventure']['scene'][0]:

        if 'title_pic_dir' in story['adventure']['scene'][0]['title']:
            title_pic_dir = story['adventure']['scene'][0]['title']['title_pic_dir']
        else:
            exit("missing title_pic_dir tag!!!")

        # check to see if save tag is in scene 0 + initialization
        if 'save_name' in story['adventure']['scene'][0]['title']:
            save_name = story['adventure']['scene'][0]['title']['save_name'] + "_save"
        else: 
            exit("missing save_name tag!!!")

         # check to see if save tag is in scene 0 + initialization
        if 'title_pic_color' in story['adventure']['scene'][0]['title']:
            title_pic_color = story['adventure']['scene'][0]['title']['title_pic_color'] 
        else: 
            exit("missing title_pic_color tag!!!")
        # check to see if save tag is in scene 0 + initialization
        if 'menu_color' in story['adventure']['scene'][0]['title']:
            menu_color = story['adventure']['scene'][0]['title']['menu_color'] 
        else: 
            exit("missing menu_color tag!!!")

    else:
        print("missing title tag")
        exit(0)
    

    list_ps = [title_pic_dir, save_name, title_pic_color, menu_color]

    return list_ps
