import webbrowser
fname_list=[]
lname_list=[]
name=[]
f=open("C:/Users/intel/Desktop/assignment/customerdata.txt","r")
l=f.read().split()                                                  #making the file data readable.
l=list(l)                                                           #converting file text into list.

for i in range(0,4):                                                #loop to remove the first line i.e. Date, Number, Name, Order amount.
    l.pop(0)

new_list=[l[i:i+5] for i in range(0,len(l),5)]                      #logic to make the sublist of the lists and gather data for each order into sub list.


def orders():                                                       #function to calculate the received orders on website.

   print("Total number of orders: ")
   print(len(new_list))
   print("\n")


def totamt():                                                       #function to calculate the total amount of orders.
    total_amount=0
    for i in range(0,len(new_list)):
        total_amount = total_amount + int(new_list[i][4])

    print("Total amount of all the orders: ")
    print(total_amount)
    print("\n")

def ordered_once():                                                #function to find the customers who ordered once and did not order again.

    print("List of customers who ordered once and did not order again:")

    for i in range(0,len(new_list)):
        fname_list.append(new_list[i][2])

    for i in range(0,len(new_list)):
        lname_list.append(new_list[i][3])


    for i in range(0,len(fname_list)):
        name.append(fname_list[i]+ ' ' +lname_list[i])             #logic to combine first and last name.
        name[i]=name[i].replace(',', '')

    nc1=0
    nc2=0
    nc3=0
    nc4=0
    nc5=0

    for i in range(0,len(name)):
        if name.count(name[i])==1:
            nc1+=1
            print(name[i])

    for i in range(0,len(name)):
        if name.count(name[i])==2:
            nc2+=1
            #print(name[i])

    nc2=int(nc2/2)

    for i in range(0,len(name)):
        if name.count(name[i])==3:
            nc3+=1
            #print(name[i])


    nc3=int(nc3/3)

    for i in range(0,len(name)):
        if name.count(name[i])==4:
            nc4+=1
            #print(name[i])


    nc4=int(nc4/4)

    for i in range(0,len(name)):
        if name.count(name[i])>=5:
            nc5+=1
            #print(name[i])


    nc5=int((nc5/5)-6)


    html_data = """
    <table border=1>
         <tr>
           <th>Orders</th>
           <th>Count of Customers</th>
         </tr>
        <tr>
            <td>1</td>
            <td>{nc1}</td>
        </tr>
        <tr>
            <td>2</td>
            <td>{nc2}</td>
        </tr>
        <tr>
            <td>3</td>
            <td>{nc3}</td>
        </tr>
         <tr>
            <td>4</td>
            <td>{nc4}</td>
        </tr>
        <tr>
            <td>5+</td>
            <td>{nc5}</td>
        </tr>
    </table>
    """.format(nc1=nc1,nc2=nc2,nc3=nc3,nc4=nc4,nc5=nc5)


    fh=open("C:/Users/intel/Desktop/assignment/html_file.html","w")
    fh.write(html_data)
    fh.close()

webbrowser.open("file://C:/Users/intel/Desktop/assignment/html_file.html")   #to open the webbrowser with html file.

if __name__ == '__main__':
    orders()
    totamt()
    ordered_once()

f.close()