def average_score(scores: list[int]) -> float:
    return float( sum(scores) / len(scores) )


def pass_fail(score: int) -> str:
    if score >= 60:
        return "pass"
    else:
        return "fail"


def analyze_scores(scores: list[int]) -> None:
    for score in scores:
        result = pass_fail(score)
        print(f"Score {score} → {result}")


if __name__ == "__main__":
    scores = [95, 82, 67, 54, 100, 73]

    print("All scores:", scores)
    print("Class average:", average_score(scores))
    print()

    analyze_scores(scores)
