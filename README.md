# Virtual Learning Management System

A comprehensive web-based learning management system designed to facilitate online education with features for both administrators and users (teachers and students).

## Features

### Admin Panel
- **Admissions Management**
  - Create and manage university admissions
  - Set admission criteria and requirements
  - Manage admission payments
  - Set seat limits for each program
  - Enroll students in courses

- **Academic Management**
  - Set up semester system
  - Create and manage yearly academic calendar
  - Manage courses and programs

- **User Management**
  - Onboard teachers and staff
  - Manage teacher/staff salaries
  - Assign unique IDs to teachers and students
  - Manage user roles and permissions

- **Notifications**
  - System-wide announcements
  - Important updates and alerts

### Teacher Portal
- **Course Management**
  - Create and manage courses
  - Upload lectures and course materials
  - Create and grade assignments
  - Create and manage quizzes

- **Class Management**
  - Create and manage class schedules
  - Conduct live sessions
  - Track student attendance
  - Manage student grades and results

- **Assessment**
  - Set exam criteria
  - Define passing marks
  - Generate and publish results
  - Provide feedback to students

### Student Portal
- **Learning**
  - Access course materials and lectures
  - View and submit assignments
  - Take quizzes and exams
  - Track learning progress

- **Academic Management**
  - View class schedule
  - Check attendance records
  - View grades and results
  - Access academic calendar

- **Account Management**
  - View and pay fees
  - Check payment status
  - Update personal information
  - View academic progress

## Technology Stack

### Backend
- Python 3.11
- Django 5.2.4
- Django REST Framework 3.16.0
- PostgreSQL (Database)
- Redis (Caching & Task Queue)

### Authentication & Security
- JWT (JSON Web Tokens)
- bcrypt for password hashing
- Role-based access control

## Getting Started

### Prerequisites
- Python 3.11
- PostgreSQL
- Redis
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd virtual-learning
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root and add the following:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/virtual_learning
   REDIS_URL=redis://localhost:6379/0
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
virtual-learning/
├── apps/
│   ├── users/           # User authentication and profiles
│   ├── admissions/      # Admission management
│   ├── academics/       # Academic programs and courses
│   ├── assessments/     # Exams and quizzes
│   ├── calendar/        # Academic calendar
│   ├── finance/         # Fee management
│   └── notifications/   # System notifications
├── virtual_learning/    # Project settings
└── manage.py            # Django management script
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.