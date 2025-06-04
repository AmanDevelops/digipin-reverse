## DIGIPIN REVERSE

Digipin Reverse is a FastAPI based application to convert the Standardized DigiPIN to an actual Human Readable Address. This application will use OpenStreetmap's [Nominatim API](https://nominatim.org/) to perform the desired action. Nominatim is the geocoding software that powers the official OSM site www.openstreetmap.org. It serves 30 million queries per day on a single server. 

# Installation
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
