# Tissue: Facial Comparison API

## Usage


### Add a face or picture
```
POST /addface HTTP/1.1
Content-Type: application/json
{
    "image":" https://media.kairos.com/kairos-elizabeth.jpg ",
    "subject_id":"Elizabeth",
    "gallery_name":"MyGallery",
    "selector":"liveness"
}
```

### Recognize a face
```
POST /recognize HTTP/1.1
Content-Type: application/json
{
    "image":" https://media.kairos.com/kairos-elizabeth.jpg ",
    "gallery_name":"MyGallery"
}
```

### Verify if face is of a certain person
```
POST /verify HTTP/1.1
Content-Type: application/json
{
    "image":" https://media.kairos.com/kairos-elizabeth2.jpg ",
    "gallery_name":"MyGallery",
    "subject_id":"Elizabeth"
}
```


