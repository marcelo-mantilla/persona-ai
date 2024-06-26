from openai import OpenAI
import tweepy
from langchain.prompts import PromptTemplate

from src.services.service import Service
from src.avatar.models import Avatar


class ImageService(Service):
    def __init__(self, avatar: Avatar, action: str, caption: str):
        self.avatar = avatar
        self.action = action
        self.caption = caption

    def generate_image(self):
        prompt_template = self._image_prompt_template()
        prompt = prompt_template.format(
            avatar_name=self.avatar.name,
            persona_template=self.avatar.persona_template.as_prompt(),
            visual_aesthetic=self.avatar.image_template.as_prompt(),
            action=self.action,
            caption=self.caption
        )

        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens= 400
        )
        generated_prompt = response.choices[0].message.content
        formatted_prompt = self.format_dalle3_prompt(generated_prompt)

        response = client.images.generate(
            model="dall-e-3",
            prompt=formatted_prompt,
            size="1024x1024",
            quality="standard",
            n=1  # TODO: parameterize
        )
        image_url = response.data[0].url
        revised_prompt = response.data[0].revised_prompt

        return image_url, revised_prompt

    @staticmethod
    def _image_prompt_template() -> PromptTemplate:
        f"""
            This constructs the image to be generated by DALL-E 3. The image prompt is constructed as follows: 
            Image = Persona + Action + Caption + ImageTemplate
        """

        return PromptTemplate.from_template(
            """
            {persona_template}
            {avatar_name} is performing the following action, to be posted on social media: {action} \n\n
            The caption that {avatar_name} has decided to go with is: {caption} \n\n
            The visual aesthetic of {avatar_name} is as follows: {visual_aesthetic}
            
            Generate a PROMPT that encapsulates {avatar_name} executing the specified action to be posted on
            social media. Please include the ENTIRE VISUAL AESTHETIC in your prompt to ensure image consistency across
            various social media posts. Find ways to creatively leverage the visual aesthetic in your prompt to imbue
            the image with creativity and emotion.
            """
        )

    @staticmethod
    def format_dalle3_prompt(dalle3_prompt: str):
        return f"""
            THIS PROMPT HAS BEEN GENERATED BY GPT4. PLEASE DO NOT MODIFY THE PROMPT, OR MODIFY AS LITTLE AS POSSIBLE:\n\n
            {dalle3_prompt}
        """
