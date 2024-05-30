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

- N1: Create fully normalised database with tables
- N2: Allow user to create an account
- N3: Allow user to log into account
- N4: Allow user to edit account information
- N5: Allow user to only view and edit own observations

### Information overview

#### User
- Username: text
- Password hash: text

#### Observation
- Plant species: text
- Observation location: GPS co-ordinate
- Observation time: date
- Photograph: image file

### Relationships
User < Observation (one to many)

### Technology stack

- Frontend: React
  - Backend API interface: Fetch API
- Backend: FastAPI
  - Database interface: SQLModel
- Database: SQLite

![technology_stack drawio](https://github.com/daveohua/floretum/assets/44324755/0d6232eb-9dea-4258-98f2-78300b7ccbca)



Third-party APIs/Libraries:

- Flower recognition API: Plant.id
- EXIF data library: Pillow
- Map integration: Leaflet
- Location autocomplete API: Pelias
