# Student Discount Platform (MVP)
## Digital Discount Verification System

A streamlined platform for managing and verifying student discounts, replacing traditional physical ID cards with a QR-based verification system.

## Core Features

### User Management
* Registration and authentication system
* Profile management and updates
* Role-based access control
  * Student accounts
  * Business accounts
  * Administrator accounts

### Student Verification System
* Document upload functionality
* Payment processing integration
* Administrator verification workflow
* QR code generation for approved students

### Discount Management
* QR code scanning for eligibility checks
* Deal listing and display
* Administrator deal controls:
  * Add new deals
  * Modify existing deals
  * Remove outdated deals

### Administrative Tools
* User verification request processing
* Deal management interface
* Permission control system
* Operation logging:
  * Verification activities
  * Deal modifications
  * Discount usage

## Technical Setup

### Environment Requirements
* Docker and docker-compose
* Git
* Python 3.x (for local development)

### Installation

```bash
# Clone repository
git clone git@github.com:ADA-OOAD-EconoME/EconoME.git

# Setup environment files
# Create and configure:
# - django.env
# - db_main.env

# Deploy with Docker
sudo docker-compose -f docker-compose-db.yml up -d --build
sudo docker-compose -f docker-compose-main-app.yml up -d --build
```

### Local Development
```bash
# Virtual environment setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run development server
bash run.sh

# Create admin account
bash account.sh
```

## Environment Configuration

### Required Environment Files
* django.env: Core settings and credentials
* db_main.env: Database configuration

### Database Setup
```env
POSTGRES_USER=test
POSTGRES_PASSWORD=test_pass
POSTGRES_DB=test_mvp
```

## Development Notes
* Debug mode available via django.env
* Built-in logging system for all operations
* Role-based permissions enforced throughout
* QR code generation and scanning enabled

## Support
For setup assistance or bug reports, please contact.

