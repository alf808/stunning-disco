# Tissue: Facial Comparison API

## Installation

**step 1:**
```
docker-compose build
docker-compose up
```

**step 2:**

Open browser and go to ```http://localhost:<port>```.

Use the data points specified in usage.

--------------
## Usage


### **Add a face or picture**
```
POST /addface HTTP/1.1
Content-Type: application/json
{
    "url":" https://en.wikipedia.org/media/alf.jpg ",
    "subject_id":"Alf",
    "gallery_name":"MyGallery",
}
```
Note: if using local file, use `file` instead of `url`


### **Recognize a face**
```
POST /recognize HTTP/1.1
Content-Type: application/json
{
    "url":" https://en.wikipedia.org/alf.jpg ",
    "gallery_name":"MyGallery"
}
```
Note: if using local file, use `file` instead of `url`


### **Verify if face is of a certain person**
```
POST /verify HTTP/1.1
Content-Type: application/json
{
    "url":" https://en.wikipedia.org/alf2.jpg ",
    "gallery_name":"MyGallery",
    "subject_id":"Alf"
}
```
Note: if using local file, use `file` instead of `url`

