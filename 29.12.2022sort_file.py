def sorteds():
    import os, datetime, time, random
    os.system('clear')
    

    list_file = []


    folders = [
        '/home/abay/Видео', 
        '/home/abay/Документы', 
        '/home/abay/Загрузки', 
        '/home/abay/Изображения', 
        '/home/abay/Музыка', 
        '/home/abay/Рабочий\ стол', 
        '/home/abay/Шаблоны', 
        '/home/abay'
    ]

    
    photo_expansion = [
        'png', 'jpg', 'jpeg',
        'gif', 'HEIC', '(1).png',
        '(2).png', '(1)jpg', '(2).jpg',
        '(1).gif', '(2).gif', '(1).jpeg'
        '(2).jpeg', '(1).HEIC', '(2).HEIC0',
        '(2).HEIC', '(3).HEIC', '(4).HEIC'    
        ' (2).HEIC', ' (3).HEIC', ' (4).HEIC'
    ]
    

    video_expansion = [
        'mp4', '(1).mp4', '(2).mp4', '.mp4',
        ' mp4', ' (1).mp4', ' (2).mp4', ' .mp4',
        'MP4', '(1).MP4', '(2).MP4', '.MP4'
        ' MP4', ' (1).MP4', ' (2).MP4', '. MP4'
    ]
    

    document_expansion = [
        'pdf', 'deb', 'tgz', 'tar.xz', 'xz', 'exe', 'zip', 
        ' .pdf', ' .deb', ' .tgz', ' .tar.xz', ' .xz', ' .exe', 
        ' .zip', '(1).pdf', '(1).deb', '(1).tgz', '(1).tar.xz', 
        '(1).xz','(1).exe', '(1).zip', '(2).pdf', '(2).deb', 
        '(2).tgz', '(2).tar.xz', '(2).xz', '(2).exe', '(2).zip'
    ]
    

    music_expansion = [
         'mp3', ' .mp3', '(1).mp3', '(2).mp3', '(3).mp3', '(4).mp3',
        'MP3', ' .MP3', '(1).MP3', '(2).MP3', '(3).MP3', '(4).MP3'
                       ]
    

    agreement = input('''
_________________________________________________________________________________
|                                                                                |
|     Я пройдусь по всем перечисленным папкам (y/n)                              |
|                                                                                |
|        [ Видео     Документы    Загрузки    Изображения ]                      |
|        [ Музыка    Рабочий стол                         ]                      |
|                                                                                |
|_____________________[Введите номер папки: ''')
    
    os.system('clear')
    
    if agreement in ['y', 'yes', 'Yes', 'Y']:
        try:
            search_file = int(input('''
_________________________________________________________________________________
|                                                                                |
| Что мне проверить:                                                             |
|                                                                                |
|   1       Видео                                                                |
|   2       Документы                                                            |
|   3       Изображения                                                          |
|   4       Музыка                                                               |
|                                                                                |
|_____________[Введите что нужно отсортировать: '''))


        except ValueError:
            os.system('clear')
            return 'Прошу прощения, выберите варианты меню от 1 до 4'
            
        if search_file == 1:
            os.system('clear')
            os.system('mkdir core')
            
            with open('core/c_document.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[1]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_document.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_document.sh')
            
            with open('core/c_download.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh 
ls {folders[2]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_download.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_download.sh')
            
            with open('core/c_image.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[3]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_image.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_image.sh')
            
            with open('core/c_music.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[4]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_music.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_music.sh')
            
#           with open('core/c_dctop.bash', 'w') as create_file:
#               create_file.write(f'''#!/bin/zsh
# ls {folders[5]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_dctop.txt''')
#               os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_dctop.bash')
                

            with open('core/c_document.txt', 'r') as read_file:
                name_items1 = read_file.read().split('\n')

            for item in name_items1:
                if item.split('.')[-1] in video_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[1]}/{name_file} {folders[0]}')
                else:
                    continue
            
            with open('core/c_download.txt', 'r') as read_file:
                name_items2 = read_file.read().split('\n')
            
            for item in name_items2:
                if item.split('.')[-1] in video_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[2]}/{name_file} {folders[0]}')
                else:
                    continue

                
            with open('core/c_image.txt', 'r') as read_file:
                name_items3 = read_file.read().split('\n')

            for item in name_items3:
                if item.split('.')[-1] in video_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[3]}/{name_file} {folders[0]}')
                else:
                    continue

                
            with open('core/c_music.txt', 'r') as read_file:
                name_items4 = read_file.read().split('\n')

            for item in name_items4:
                if item.split('.')[-1] in video_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[4]}/{name_file} {folders[0]}')
                else:
                    continue
                
            # with open('core/c_desctop.txt', 'r') as read_file:
            #     name_items5 = read_file.read().split('\n')
            # for item in name_items5:
            #     if item.split('.')[-1] in video_expansion:
            #         list_file.append(item)
            #         for name_file in list_file:
            #             os.system(f'mv {folders[5]}/{name_file} {folders[0]}')
            #     else:
            #         continue     
                
            with open('core/delete_file.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
rm -rf /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core''')
    
            # os.system(f'bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/delete_file.sh')
            os.system('clear')
            return 'Программа завершила работу'


        # Задание: продолжить программу 
        #     elif search_file == 2: сортировка докумертов
        #     elif search_file == 3: сортировка изображения
        #     elif search_file == 4: сортировка музыки


        elif search_file == 2:
            os.system('clear')
            os.system('mkdir core')
            
            with open('core/c_video.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[0]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_video.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_video.sh')
            
            with open('core/c_download.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[2]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_download.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_download.sh')
            
            with open('core/c_image.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[3]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_image.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_image.sh')
            
            with open('core/c_music.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[4]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_music.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_music.sh')
            
#             with open('core/c_dctop.bash', 'w') as create_file:
#                 create_file.write(f'''#!/bin/zsh
# la {folders[5]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_dctop.txt''')
#                 os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_dctop.bash')
                

            with open('core/c_video.txt', 'r') as read_file:
                name_items1 = read_file.read().split('\n')

            for item in name_items1:
                if item.split('.')[-1] in document_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[0]}/{name_file} {folders[1]}')
                else:
                    continue
            

            with open('core/c_download.txt', 'r') as read_file:
                name_items2 = read_file.read().split('\n')

            for item in name_items2:
                if item.split('.')[-1] in document_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[2]}/{name_file} {folders[1]}')
                else:
                    continue

                
            with open('core/c_image.txt', 'r') as read_file:
                name_items3 = read_file.read().split('\n')

            for item in name_items3:
                if item.split('.')[-1] in document_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[3]}/{name_file} {folders[1]}')
                else:
                    continue

                
            with open('core/c_music.txt', 'r') as read_file:
                name_items4 = read_file.read().split('\n')

            for item in name_items4:
                if item.split('.')[-1] in document_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[4]}/{name_file} {folders[1]}')
                else:
                    continue

                
            # with open('core/c_desctop.txt', 'r') as read_file:
            #     name_items5 = read_file.read().split('\n')
            # for item in name_items5:
            #     if item.split('.')[-1] in video_expansion:
            #         list_file.append(item)
            #         for name_file in list_file:
            #             os.system(f'mv {folders[5]}/{name_file} {folders[0]}')
            #     else:
            #         continue   

                
            with open('core/delete_file.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
rm -rf /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core''')
    
            os.system(f'bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/delete_file.sh')
            os.system('clear')
            return 'Программа завершила работу'
        
        
        elif search_file == 3:
            os.system('clear')
            os.system('mkdir core')
            
            with open('core/c_video.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[0]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_video.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_video.sh')
            
            with open('core/c_download.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[2]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_download.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_download.sh')
            
            with open('core/c_documents.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[1]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_documents.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_documents.sh')
            
            with open('core/c_music.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[4]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_music.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_music.sh')
            

#             with open('core/c_dctop.bash', 'w') as create_file:
#                 create_file.write(f'''#!/bin/zsh
# la {folders[5]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_dctop.txt''')
#                 os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_dctop.bash')
                

            with open('core/c_video.txt', 'r') as read_file:
                name_items1 = read_file.read().split('\n')

            for item in name_items1:
                if item.split('.')[-1] in photo_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[0]}/{name_file} {folders[3]}')
                else:
                    continue
            

            with open('core/c_download.txt', 'r') as read_file: 
                name_items2 = read_file.read().split('\n') 

            for item in name_items2:
                if item.split('.')[-1] in photo_expansion:
                    list_file.append(item) 
                    for name_file in list_file:
                        os.system(f'mv {folders[2]}/{name_file} {folders[3]}') 
                else:
                    continue

                
            with open('core/c_documents.txt', 'r') as read_file:
                name_items3 = read_file.read().split('\n')

            for item in name_items3:
                if item.split('.')[-1] in photo_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[1]}/{name_file} {folders[3]}')
                else:
                    continue

                
            with open('core/c_music.txt', 'r') as read_file:
                name_items4 = read_file.read().split('\n')

            for item in name_items4:
                if item.split('.')[-1] in photo_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[4]}/{name_file} {folders[3]}')
                else:
                    continue

                
            # with open('core/c_desctop.txt', 'r') as read_file:
            #     name_items5 = read_file.read().split('\n')
            # for item in name_items5:
            #     if item.split('.')[-1] in video_expansion:
            #         list_file.append(item)
            #         for name_file in list_file:
            #             os.system(f'mv {folders[5]}/{name_file} {folders[0]}')
            #     else:
            #         continue   
                
            with open('core/delete_file.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
rm -rf /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core''')
    
            os.system(f'bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/delete_file.sh')
            os.system('clear')
            return 'Программа завершила работу'


        elif search_file == 4:
            os.system('clear')
            os.system('mkdir core')
            

            with open('core/c_video.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[0]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_video.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_video.sh')
            
            with open('core/c_download.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[2]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_download.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_download.sh')
            
            with open('core/c_image.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[3]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_image.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_image.sh')
            
            with open('core/documents.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
ls {folders[1]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/documents.txt''')
            os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/documents.sh')
            

#             with open('core/c_dctop.bash', 'w') as create_file:
#                 create_file.write(f'''#!/bin/zsh
# la {folders[5]} > /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_dctop.txt''')
#                 os.system('bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/c_dctop.bash')
                

            with open('core/c_video.txt', 'r') as read_file:
                name_items1 = read_file.read().split('\n')

            for item in name_items1:
                if item.split('.')[-1] in music_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[0]}/{name_file} {folders[4]}')
                else:
                    continue
            

            with open('core/c_download.txt', 'r') as read_file: 
                name_items2 = read_file.read().split('\n') 

            for item in name_items2:
                if item.split('.')[-1] in music_expansion:
                    list_file.append(item) 
                    for name_file in list_file:
                        os.system(f'mv {folders[2]}/{name_file} {folders[4]}') 
                else:
                    continue

                
            with open('core/c_documents.txt', 'r') as read_file:
                name_items3 = read_file.read().split('\n')

            for item in name_items3:
                if item.split('.')[-1] in music_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[1]}/{name_file} {folders[4]}')
                else:
                    continue
                

            with open('core/c_image.txt', 'r') as read_file:
                name_items4 = read_file.read().split('\n')

            for item in name_items4:
                if item.split('.')[-1] in music_expansion:
                    list_file.append(item)
                    for name_file in list_file:
                        os.system(f'mv {folders[3]}/{name_file} {folders[4]}')
                else:
                    continue

                
            # with open('core/c_desctop.txt', 'r') as read_file:
            #     name_items5 = read_file.read().split('\n')
            # for item in name_items5:
            #     if item.split('.')[-1] in video_expansion:
            #         list_file.append(item)
            #         for name_file in list_file:
            #             os.system(f'mv {folders[5]}/{name_file} {folders[0]}')
            #     else:
            #         continue   

                

            with open('core/delete_file.sh', 'w') as create_file:
                create_file.write(f'''#!/bin/zsh
rm -rf /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core''')
    

            os.system(f'bash /home/abay/lessons/Python\ Bootcamp/29.12.2022_sort_file/core/delete_file.sh')
            os.system('clear')
            return 'Программа завершила работу'



print(sorteds()) 

