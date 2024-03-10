from bot_manager.bot_step import Step

import pytz 
import datetime
import dateutil.parser

class ChatGPTPrompt(Step):

    async def process(self, payload):
        messages=payload['messages']

        payload['chatml'] = self._chatml(messages)

        return payload
    
    def _dress_content(self, message):
        content = message['body']

        if message["user"] != self.bot_name:
            if 'each_user_message' in self.config:
                content = self.config.each_user_message.replace('{content}', content)
            
            input_time = dateutil.parser.parse(message['timestamp'])
            target_tz = pytz.timezone("Australia/Melbourne")
            melbourne_time = input_time.astimezone(target_tz)

            content = content.replace('{timestamp}', str(melbourne_time))            
        
        return content 

    def _format_chatml(self, message, bot_name):
        
        chat_ml = { 
            "content": self._dress_content(message),
            "name": message["user"],
            "role": "assistant" if message["user"] == bot_name else "user"
         }

        return chat_ml
    
    def _chatml(self, messages):
        results = [self._format_chatml(message, self.bot_name) for message in messages]
        
        return results

if __name__ == "__main__":
    ChatGPTPrompt.main()