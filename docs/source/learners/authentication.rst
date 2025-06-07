Authentication
==================
Some models on Hugging Face require authentication. You can provide your Hugging Face token in several ways:
1. **Environment Variable**: Set the `HUGGINGFACE_ACCESS_TOKEN` environment variable
2. **Direct Parameter**: Pass the token directly to the constructor:

   .. code-block:: python

       llm = AutoLearnerLLM(token="your_huggingface_token")

3. **.env File**: Create a `.env` file with your token:

   .. code-block:: text

       HUGGINGFACE_ACCESS_TOKEN=your_huggingface_token

   Then load it in your script:

   .. code-block:: python

       from dotenv import find_dotenv, load_dotenv
       _ = load_dotenv(find_dotenv())
