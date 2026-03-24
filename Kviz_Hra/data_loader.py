"""
Data loading utilities for Kviz_Hra
"""

import json
import os
from typing import List, Optional
from models import Question
import config


class DataLoader:
    """Manager for loading and validating question data"""

    def __init__(self, questions_file: str = config.QUESTIONS_FILE):
        self.questions_file = questions_file
        self.questions: List[Question] = []
        self.loaded = False

    def load_questions(self) -> bool:
        """
        Load questions from JSON file.
        Returns True if successful, False otherwise.
        """
        if not os.path.exists(self.questions_file):
            print(f"Questions file not found: {self.questions_file}")
            return False

        try:
            with open(self.questions_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.questions = []
            
            # Handle both direct list and nested structure
            questions_data = data.get('questions', data) if isinstance(data, dict) else data

            for q in questions_data:
                try:
                    question = Question(
                        id=q.get('id', f"q_{len(self.questions)}"),
                        title=q.get('title', q.get('answer', 'Unknown')),
                        image_path=q.get('image_path', q.get('image', '')),
                        answer=q.get('answer', ''),
                        category=q.get('category', 'General'),
                        difficulty=q.get('difficulty', 1),
                        description=q.get('description', '')
                    )
                    
                    # Validate image path
                    if question.image_path and not question.image_path.startswith('/'):
                        question.image_path = os.path.join(config.IMAGES_DIR, question.image_path)

                    self.questions.append(question)
                except Exception as e:
                    print(f"Error loading question: {e}")
                    continue

            self.loaded = len(self.questions) > 0
            print(f"Loaded {len(self.questions)} questions")
            return self.loaded

        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return False
        except Exception as e:
            print(f"Error loading questions: {e}")
            return False

    def get_question(self, index: int) -> Optional[Question]:
        """Get a specific question by index"""
        if 0 <= index < len(self.questions):
            return self.questions[index]
        return None

    def get_question_by_id(self, question_id: str) -> Optional[Question]:
        """Get a specific question by ID"""
        for q in self.questions:
            if q.id == question_id:
                return q
        return None

    def get_all_questions(self) -> List[Question]:
        """Get all loaded questions"""
        return self.questions

    def get_questions_by_category(self, category: str) -> List[Question]:
        """Get all questions in a specific category"""
        return [q for q in self.questions if q.category == category]

    def get_questions_by_difficulty(self, difficulty: int) -> List[Question]:
        """Get all questions of a specific difficulty level"""
        return [q for q in self.questions if q.difficulty == difficulty]

    def save_results(self, game_state_dict: dict, filename: str = None) -> bool:
        """
        Save game results to JSON file in results directory.
        If filename is None, generates one from timestamp.
        """
        import datetime
        
        if filename is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"result_{timestamp}.json"

        filepath = os.path.join(config.RESULTS_DIR, filename)

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(game_state_dict, f, indent=2, ensure_ascii=False)
            print(f"Results saved to {filepath}")
            return True
        except Exception as e:
            print(f"Error saving results: {e}")
            return False

    def load_results(self, filename: str) -> Optional[dict]:
        """Load results from a JSON file"""
        filepath = os.path.join(config.RESULTS_DIR, filename)

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading results: {e}")
            return None
