from typing import List


def average_score(scores: List[int]) -> float:
    return sum(scores) / len(scores)


def pass_fail(score: int) -> str:
    if score >= 60:
        return "pass"
    else:
        return "fail"


def analyze_scores(scores: List[int]) -> None:
    for score in scores:
        result = pass_fail(score)
        print(f"Score {score} → {result}")


if __name__ == "__main__":
    scores = [95, 82, 67, 54, 100, 73]

    print("All scores:", scores)
    print("Class average:", average_score(scores))
    print()

    analyze_scores(scores)
