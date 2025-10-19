# Development Setup

### Local Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create the local database:
   ```bash
   mysql -u root -p < schema.sql
   ```
3. Run the robots audit:
   ```bash
   python robots_audit.py
   ```
4. Load mock data:
   ```bash
   python load_mock_data.py
   ```

*For internal EcoServants® testing only.*
