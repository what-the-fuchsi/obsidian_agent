import pytest
import os
import yaml
from pathlib import Path
from unittest.mock import patch, MagicMock

import obsidian_agent.ai_providers as ai_providers


def test_config_loading():
    # Ensure config loads and has expected keys
    assert ai_providers.MAX_TOKENS > 0
    assert isinstance(ai_providers.INITIAL_PROMPT, str)

def test_secret_loading():
    # Ensure secret config loads and API key is present
    assert isinstance(ai_providers.api_key, str)
    assert len(ai_providers.api_key) > 10

def test_secret_path_expansion():
    # The secret path should be expanded and exist
    raw_path = ai_providers.config.get('secret-config-path')
    expanded = os.path.expandvars(raw_path)
    path_obj = Path(expanded)
    assert path_obj.exists()

def test_generate_content_mocks_openai():
    # Patch openai.OpenAI and its methods
    with patch('openai.OpenAI') as mock_openai:
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content='Test output'))]
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        result = ai_providers.generate_content('test prompt', api_key_override='sk-test')
        assert result == 'Test output'
        mock_openai.assert_called_with(api_key='sk-test') 