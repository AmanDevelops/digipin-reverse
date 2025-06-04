## DIGIPIN REVERSE

Digipin Reverse is a FastAPI based application to convert the Standardized DigiPIN to an actual Human Readable Address. This application will use OpenStreetmap's [Nominatim API](https://nominatim.org/) to perform the desired action. Nominatim is the geocoding software that powers the official OSM site www.openstreetmap.org. It serves 30 million queries per day on a single server. 

# 🚀 API Usage

## Decode DigiPIN to Address
```
GET /reverse/378-KLJ-T68K
```
### Response 
``` json
{
  "success": true,
  "response": {
    "place_id": 225662670,
    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. http://osm.org/copyright",
    "osm_type": "way",
    "osm_id": 209442232,
    "lat": "26.8467168",
    "lon": "80.9461596",
    "category": "highway",
    "type": "primary",
    "place_rank": 26,
    "importance": 0.05340235523002972,
    "addresstype": "road",
    "name": "Hazratganj",
    "display_name": "Hazratganj, Lucknow, Uttar Pradesh, 226027, India",
    "address": {
      "road": "Hazratganj",
      "suburb": "Hazratganj",
      "city": "Lucknow",
      "county": "Lucknow",
      "state_district": "Lucknow",
      "state": "Uttar Pradesh",
      "ISO3166-2-lvl4": "IN-UP",
      "postcode": "226027",
      "country": "India",
      "country_code": "in"
    },
    "boundingbox": [
      "26.8465726",
      "26.8468647",
      "80.9459946",
      "80.9463245"
    ],
    "digipin": "378-KLJ-T68K"
  }
}
```


### Interactive API Documentation

Access the Swagger UI documentation at:

```
http://localhost:8000/docs
```

---

# 📦 Installation
## Step 1: Boot up your Nominatim Server
### For Small Projects 
Use the API, make sure to read its [usage policy](https://operations.osmfoundation.org/policies/nominatim/)
- No heavy uses (an absolute maximum of 1 request per second).
- Provide a valid HTTP Referer or User-Agent identifying the application (stock User-Agents as set by http libraries will not do).
- ***Clearly display attribution as suitable for your medium.***
- Data is provided under the ODbL license which requires to share alike (although small extractions are likely to be covered by fair usage / fair dealing).

  ``` bash
  NOMINATIM_BASE_URL=https://nominatim.openstreetmap.org
  ```

### For Production Scale Projects

Self-Host Your Own Server [Instructions](https://nominatim.org/release-docs/latest/admin/Installation/)


## Step 2: Clone The repository

``` bash
git clone https://github.com/AmanDevelops/digipin-reverse.git
cd digipin-reverse
```
## Step 3: Setup the `.env` file
``` env
USER_AGENT="YourAppName/1.0 (your_email@example.com)"
NOMINATIM_BASE_DOMAIN=https://your_nominatim_server.com
```

## Step 4: Start with Docker Compose
``` bash
docker compose -f 'docker-compose.yml' up -d --build 'app'
```
## Step 5: Verify the installation

Visit `http://localhost:8000/docs` on your browser

---
 
## 🔧 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code adheres to the existing style and passes all tests.
