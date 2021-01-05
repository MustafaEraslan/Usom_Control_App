import requests
responce=requests.get("https://www.usom.gov.tr/url-list.txt",verify=False) #https'i ssl'ı gözardı etmek için kullanıyoruz
dosya=open("usom.txt","w")
dosya.write(str(responce.content)) #dosya içeriğini yaz
dosya.close()
#usom txt oluşturularak zararlı alan adları görüntülenmiş oldu


