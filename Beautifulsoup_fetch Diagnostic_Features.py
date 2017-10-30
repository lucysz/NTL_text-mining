from bs4 import BeautifulSoup
import requests 

url = ["http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm01",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm02",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm03",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm04",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm05",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm06",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm07",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm08",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm09",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm10",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm11",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm12",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm13",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm14",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm15",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm16",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm17",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm18",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm19",
       "http://dsm.psychiatryonline.org/doi/full/10.1176/appi.books.9780890425596.dsm20"]
    

def main():
   
    for i in range(len(url)):
        r = requests.get(url[i])
        soup = BeautifulSoup(r.content, "html.parser")
        j = 1
        d_features = soup.findAll("div",class_="APP-DiagnosticFeatures")
        if d_features == []:
            file.write("\n")
        else:
            for d in d_features:
                txt = d.text
                txt = txt[21:]
                file = open("dsm5_chapt"+str(i+1)+"diagnosis"+str(j)+".txt","w",encoding="utf-8")
                file.write(txt)
                file.write("\n")
                file.close()
                j += 1
                

##my_file = open("dsm5_chapt"+str(19)+".txt","r",encoding="utf-8")
##
##all_txt = my_file.readlines()
##for i in all_txt:
##    print(i)
##    print("\n")
##    print("\n")
##    print("\n")
    
    
main()
