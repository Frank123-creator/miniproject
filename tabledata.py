from seleniumrun import search
def tabledata(search_query1,search_query2):
    productnames1,technology1,announce1,status1,dimensions1,weight1,build1,sim1,type1,size1,resolution1,os1,chipset1,cpu1,gpu1,cardslot1,internal1,single1,features1,video1,s_ingle1,f_eatures1,v_ideo1,loudspeaker1,jack1,waln1,blutooth1,positioning1,nfc1,radio1,usb1,sensors1,type_1,charging1,colors1,img_url1 = search(search_query1)
    productnames2,technology2,announce2,status2,dimensions2,weight2,build2,sim2,type2,size2,resolution2,os2,chipset2,cpu2,gpu2,cardslot2,internal2,single2,features2,video2,s_ingle2,f_eatures2,v_ideo2,loudspeaker2,jack2,waln2,blutooth2,positioning2,nfc2,radio2,usb2,sensors2,type_2,charging2,colors2,img_url2 = search(search_query2)
    table_data=[{'data1':productnames1,'data2':technology1,'data3':announce1,'data4':status1,'data5':dimensions1,'data6':weight1,'data7':sim1,'data8':type1,'data9':size1,'data10':resolution1,'data11':os1,'data12':chipset1,'data13':cpu1,'data14':gpu1,'data15':cardslot1,'data16':internal1,'data17':single1,'data18':features1,'data19':video1,'data20':s_ingle1,'data21':f_eatures1,'data22':v_ideo1,
                         'data23':loudspeaker1,'data24':jack1,'data25':waln1,'data26':blutooth1,'data27':positioning1,'data28':nfc1,'data29':radio1,'data30':usb1,'data31':sensors1,'data32':type_1,'data33':charging1,'data34':colors1,
                         'data35':productnames2,'data36':technology2,'data37':announce2,'data38':status2,'data39':dimensions2,'data40':weight2,'data41':sim2,'data42':type2,'data43':size2,'data44':resolution2,'data45':os2,'data46':chipset2,'data47':cpu2,'data48':gpu2,'data49':cardslot2,
                         'data50':internal2,'data51':single2,'data52':features2,'data53':video2,'data54':s_ingle2,'data55':f_eatures2,'data56':v_ideo2,'data57':loudspeaker2,'data58':jack2,'data59':waln2,'data60':blutooth2,'data61':positioning2,'data62':nfc2,'data63':radio2,'data64':usb2,'data65':sensors2,'data66':type_2,'data67':charging2,'data68':colors2,'data69':build1,'data70':build2,'data71':img_url1,'data72':image_url2  
                         }   
            ]
    return table_data
