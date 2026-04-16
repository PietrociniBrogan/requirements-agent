from requirements_agent.config import Config, validate_config


def main() -> None:
    validate_config()
    print("Project setup is working.")
    print(f"Model: {Config.MODEL_NAME}")


if __name__ == "__main__":
    main()