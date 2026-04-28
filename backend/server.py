import sys
import os  
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

print("--- Gemini API Server is starting ---")

@app.route('/optimize', methods=['POST'])
def optimize_code():
    print("\n--- Received a request ---")
    
    if not request.json or 'code' not in request.json:
        print("Request error: No 'code' key in JSON.")
        return jsonify({'error': 'No code provided'}), 400

    user_prompt = request.json['code']
    print(f"Received prompt length: {len(user_prompt)} chars") 

    try:
    
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise Exception("GOOGLE_API_KEY secret is not set.")
       
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

        payload = {
            "contents": [{
                "parts": [{ "text": user_prompt }]
            }]
        }

        print("Sending request to Gemini API...")
        
        response = requests.post(api_url, json=payload, headers={'Content-Type': 'application/json'})
        response.raise_for_status() 
        
        result = response.json()

        optimized_code = result['candidates'][0]['content']['parts'][0]['text']
        
        print("Optimization generated successfully.")
        
        return jsonify({'optimization': optimized_code})

    except Exception as e:
        print(f"--- ERROR during Gemini API call: {e} ---")
        return jsonify({'error': f'Prediction failed: {e}'}), 500

if __name__ == '__main__':
  
    app.run(host='0.0.0.0', port=7860)
