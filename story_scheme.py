Pic_dir = ""
save_name = ""
list_ps = [ ]

def check(story: dict, Pic_dir: str, save_name: str):
    # check to see if title tag is in scene 0 + initialization
    if 'title' in story['adventure']['scene'][0]:
        Pic_dir = story['adventure']['scene'][0]['title']
    else:
        print("missing title tag")
        exit(0)
    # check to see if save tag is in scene 0 + initialization
    if 'save_name' in story['adventure']['scene'][0]:
        save_name = story['adventure']['scene'][0]['save_name'] + "_save"
    else: 
        exit("missing save_name tag!!!")

    list_ps = [Pic_dir, save_name]

    return list_ps
