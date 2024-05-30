# Requirements

### Overview

A web application that allows users to document their observations of plants in various locations throughout the year.

### Functional requirements

#### Minimum viable product

- F1: Record plant observations: species, observation location, observation time, and an uploaded photograph
- F2: View a list of all recorded observations, sorted alphabetically by species or date/time
- F3: View, edit and delete individual observations.

#### Further enhancements

- F4: Autocomplete observation locations
- F5: Plant species recognition from uploaded photograph
- F6: Observation location and date/time detection from photo EXIF data
- F7: View observations on an interactive map

### Non-functional requirements

#### Minimum viable product

- N1: Allow user to create an account
- N2: Allow user to log into account
- N3: Allow user to edit account information
- N4: Allow user to only view and edit own observations

### Technology stack

- Frontend: React
- Backend: FastAPI
- Database: SQLite

Third-party APIs/Libraries:

- Flower recognition API: Plant.id
- EXIF data library: Pillow
- Map integration: Leaflet
- Location autocomplete API: Pelias

## 