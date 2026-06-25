# Uneeq Voice Assistant

A lightweight, local voice assistant prototype written in Python. It listens to the microphone, transcribes speech, matches intents from a small knowledge base, and speaks responses.

---

## Features

- Keyword-based intent matching with simple scoring
- Voice input via `speech_recognition` and Whisper (via the `recognize_whisper` API)
- Speech output via `pyttsx3`
- Dynamic responses (time, date, jokes) and a `repeat` action
- Simple, easy-to-extend `brain/intent.py` knowledge base

---

## Repository Structure

- `main.py` — app entrypoint and main loop
- `stt.py` — speech-to-text helpers (microphone, calibration, transcription)
- `tts.py` — text-to-speech output wrapper
- `brain/assistant.py` — intent matching and response selection logic
- `brain/intent.py` — intents, keyword lists, and response functions
- `requirements.txt` — Python dependencies
- `to_be_added.md` — planned features / future work

---

## Prerequisites

- Python 3.11+ recommended
- A working microphone and speakers
- On Windows: ensure you have an audio driver and permissions for microphone access

Optional but recommended:
- A virtual environment for project isolation

---

## Installation

1. Clone the repo and change into the project folder.

2. Create and activate a virtual environment (example for Windows PowerShell):

```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

Notes:
- If `speech_recognition` or `pyttsx3` require additional system packages on your platform, follow their official installation notes.
- The project uses Whisper through the `speech_recognition` recognizer's `recognize_whisper` method; ensure your environment supports that API or replace it with an alternative recognizer.

---

## Usage

Run the assistant from the project root:

```powershell
python main.py
```

Behavior:
- The assistant will calibrate background noise, greet you, then enter a listening loop.
- Speak a command or question. If the assistant cannot detect audio it will retry the listening loop.
- Say an exit word (e.g., "bye", "goodbye", "exit") to stop the assistant.

Example utterances and expected behavior:

- "What time is it?" → assistant responds with current time
- "Tell me a joke" → assistant chooses a random joke
- "Repeat after me hello world" → assistant repeats the phrase after the trigger
- "Goodbye" → assistant says goodbye and stops after the response

---

## Intents and Extending Behavior

Intents are defined in `brain/intent.py`. Each intent contains:
- `name`: short identifier
- `keywords`: list of trigger phrases or words
- `response`: either a static string or a function that returns a string

To add a new intent:
1. Open `brain/intent.py` and add a new dict to the `INTENTS` list.
2. Add any helper response functions above the `INTENTS` list if you need dynamic output.
3. Restart the assistant to load changes.

The matching algorithm in `brain/assistant.py` performs a simple score by summing the matched keyword lengths. You can replace `match_intent()` with a more sophisticated NLP matcher (embedding/semantic search, fuzzy matching, etc.) if needed.

---

## Development

- Keep tests and experiment code separate if you add them.
- Use a feature branch for larger features (e.g., weather integration).
- Update `to_be_added.md` when planning new features.

Recommended next improvements (already noted in `to_be_added.md`):
- Weather feature (API integration)
- Offline speech recognition alternative for environments without Whisper

---

## Troubleshooting

- If the assistant cannot hear you: check microphone permissions and that the correct input device is selected at the OS level.
- If `recognize_whisper` raises errors: ensure your `speech_recognition` version supports Whisper or replace the recognizer call.
- If TTS is silent: check `pyttsx3` backend on your platform and set a supported voice.

---

## Contributing

1. Fork the repo and create a feature branch.
2. Make your changes and test locally.
3. Open a pull request with a clear description of changes.

Please follow the existing style and keep changes focused.

---

## License

This project does not include an explicit license file. Add a `LICENSE` at the project root to make licensing clear.

---

## Acknowledgements

- Built as a simple educational prototype.
