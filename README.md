# Multi-Branch Customer Service Chatbot

A Rasa-powered chatbot that handles customer inquiries for both ecommerce and banking services. This chatbot can seamlessly switch between different business domains and provide specialized support for each.

## Features

### Ecommerce Support
- Order status tracking
- Product information lookup
- Return and refund assistance
- Shipping inquiries
- Payment issue resolution

### Banking Support
- Account balance checking
- Transaction history
- Money transfers
- Loan inquiries
- Card services
- Account management

## Installation

1. **Install Python 3.8 or higher**

2. **Install Rasa and dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model:**
   ```bash
   rasa train
   ```

4. **Start the action server (in a separate terminal):**
   ```bash
   rasa run actions
   ```

5. **Start the chatbot (in another terminal):**
   ```bash
   rasa shell
   ```

## Usage

### Starting the Chatbot

1. **Train the model first:**
   ```bash
   rasa train
   ```

2. **Run the action server:**
   ```bash
   rasa run actions --actions actions.actions
   ```

3. **Start the chatbot:**
   ```bash
   rasa shell
   ```

### Example Conversations

**Ecommerce Inquiry:**
```
User: Hello, I need help with my order
Bot: Welcome to our ecommerce support! I can help you with order status, product information, returns, shipping, and payment questions.
User: Where is my order 12345?
Bot: I'd be happy to help you check your order status. Could you please provide your order number?
```

**Banking Inquiry:**
```
User: I need banking help
Bot: Welcome to our banking support! I can help you with account balance, transactions, transfers, loans, and card-related inquiries.
User: Check my balance for account 123456
Bot: I can help you check your account balance. For security purposes, I'll need to verify your account information first.
```

## Project Structure

```
├── actions/
│   └── actions.py          # Custom actions for complex interactions
├── data/
│   ├── nlu.yml            # Training data for NLU
│   ├── stories.yml        # Conversation stories
│   └── rules.yml          # Response rules
├── config.yml             # Rasa configuration
├── domain.yml             # Domain definition
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Customization

### Adding New Intents
1. Add new intent to `domain.yml`
2. Add training examples in `data/nlu.yml`
3. Create stories in `data/stories.yml`
4. Add rules in `data/rules.yml`

### Adding New Actions
1. Create new action class in `actions/actions.py`
2. Add action name to `domain.yml`
3. Reference the action in stories or rules

### Modifying Responses
Edit the responses in `domain.yml` under the `responses` section.

## Testing

Test the chatbot by running:
```bash
rasa test
```

## Deployment

For production deployment, consider using:
- Rasa X for conversation management
- Docker for containerization
- Cloud platforms like AWS, GCP, or Azure

## Security Notes

- The current implementation uses mock data for demonstration
- In production, implement proper authentication and data validation
- Ensure secure handling of sensitive banking information
- Use encrypted connections for all API calls

## Support

For issues or questions about this chatbot implementation, please refer to the Rasa documentation or create an issue in the project repository.




