from flask import Flask, render_template, request
import json
import csv, os
app = Flask( __name__ )


def create_index_list(nested_lst):
    index = 0
    lst = []
    for nested in nested_lst:
        lst += [index]
        index += 1
    return lst

#def import_csv(csv_file):
#   with open(csv_file, 'r') as file:
#        csvreader = csv.reader(file)
#        next(csvreader)
#        msg = []
#        for row in csvreader:
#            msg += [row]
#    return msg

@app.route('/', methods=['GET'])
def entry():
    info = {}
    with open("static/e-waste-coords.csv") as csvfile:
        csvreader=csv.reader(csvfile)
        next(csvreader)
        for i in csvreader:
            info.update({i[0]:{"lat":i[7],"lon":i[8],"website":i[5],"description":i[10]}})
    corres_coord = {}
    corres_details = {}
    lstofalgos = {"greedy1":"greedy2.csv","greedy2":"greedy3.csv","ouralgo1":"ouralgo--worse.csv","ouralgo2":"ouralgo--normal.csv","ouralgo3":"ouralgo3ver3--noswap.csv","ouralgo4":"ouralgo3ver3--best.csv"}
    for key,value in lstofalgos.items():
        lst_of_coords = [] 
        details = []
        with open("static/"+value) as csvfile:
            csvreader = csv.reader(csvfile)
            truckcount = 0
            next(csvreader)
            for i in csvreader:
                truckcount+=1
                coordlst=[]
                detaillst = []
                truckno = i[0]
                for point in i[1:]:
                    if point == "": continue
                    info_row = info[point]
                    detaillst.append([f"Truck {truckno}",info_row["description"],info_row["website"]])
                    coordlst.append([float(info_row["lon"]),float(info_row["lat"])])
                lst_of_coords.append(coordlst)
                details.append(detaillst)
        print(len(lst_of_coords))
        corres_coord.update({key:lst_of_coords})
        corres_details.update({key:details})
    #curr_dir = os.path.dirname(os.path.abspath(__file__))
    #file_name = os.path.join(curr_dir, "static/{}".format(lst_of_coords))
    #coords = import_csv(file_name)
    
    return render_template('entry.html', lst_of_coords = corres_coord, details = corres_details, index_list = [1,2,3,4,5])

if __name__ == '__main__':
  app.run(port=8080, host='0.0.0.0', debug=True)



#coords used previously, paste into the part marked
#[[-122.483696, 37.833818],
#	[-122.483482, 37.833174],
#	[-122.483396, 37.8327],
#	[-122.483568, 37.832056],
#	[-122.48404, 37.831141],
#	[-122.48404, 37.830497],
#	[-122.483482, 37.82992],
#	[-122.483568, 37.829548],
#	[-122.48507, 37.829446],
#	[-122.4861, 37.828802],
#	[-122.486958, 37.82931],
#	[-122.487001, 37.830802],
#	[-122.487516, 37.831683],
#	[-122.488031, 37.832158],
#	[-122.488889, 37.832971],
#	[-122.489876, 37.832632],
#	[-122.490434, 37.832937],
#	[-122.49125, 37.832429],
#	[-122.491636, 37.832564],
#	[-122.492237, 37.833378],
#	[-122.493782, 37.833683]
#	]

#
#
#
#'<h5 style = "margin:0;">{{details[i][coord_idx][0]}}</h5><h5 style = "margin:0;">{{details[i][coord_idx][1]}}</h5><h5 style = "margin:0;">{{details[i][coord_idx][2]}}</h5><h5 style = "margin:0;">{{details[i][coord_idx][3]}}</h5><h5 style = "margin:0;">{{details[i][coord_idx][4]}}</h5><h5 style = "margin:0;">{{details[i][coord_idx][5]}}</h5>'
