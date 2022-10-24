import requests
import csv
import time
import random

key = "AIzaSyBxen4xoe88RGY-vQPu72Hwur70E1P0Ri4"
start_time = time.time()

def get_panoid(lat,lng):
    response = requests.get(f"https://maps.googleapis.com/maps/api/streetview/metadata?location={lat},{lng}&key={key}")
    data = response.text
    data = data.split(",")
    pano_id = data[4]
    pano_id = pano_id[17:]
    pano_id = pano_id[:-1]
    return pano_id

def download_from_panoID(panoID,filename):
    x = 6
    y = 2
    zoom = 3
    nbt = 4
    url = "https://geo0.ggpht.com/cbk?cb_client=apiv3&panoid={panoID}&output=tile&x={x}&y={y}&zoom={zoom}&nbt={nbt}&fover=2".format(panoID=panoID,x=x,y=y,zoom=zoom,nbt=nbt)
    with open(filename, 'wb') as handle:
        response = requests.get(url, stream=True)
        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)

def download_from_latlng(lat,lng,filename):
    panoID = get_panoid(lat,lng)
    download_from_panoID(panoID,filename)
    #print(f"Saved as {filename}")

def main():
    csv_filename = "locs.csv"
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if line_count % 5 == 0:
                    print(f"At line: {line_count}")
                lat = row[0]
                lng = row[1]
                download_from_latlng(lat,lng,"image_"+str(line_count)+".jpg")
                line_count += 1
        print(f'Processed {line_count} lines.')
        print("program took %s seconds" % (time.time() - start_time))

main()
