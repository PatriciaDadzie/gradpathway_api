from catalog.models import Programme
from .models import MatchResult

def generate_matches(match_request):
    transcript = match_request.transcript
    filters = match_request.filters or {}

    programmes = Programme.objects.all()

    # Apply filters
    if "country" in filters:
        programmes = programmes.filter(university__country__iexact=filters["country"])

    # Simple rule-based matching (based on GPA)
    matches = []
    for programme in programmes:
        if transcript.gpa and transcript.gpa >= programme.min_gpa:
            score = min(100, (transcript.gpa / programme.min_gpa) * 50 + 50)
            reasoning = f"Eligible (GPA {transcript.gpa} >= {programme.min_gpa})"
        else:
            score = 0
            reasoning = f"Below required GPA ({transcript.gpa} < {programme.min_gpa})"

        match = MatchResult(
            match_request=match_request,
            programme=programme,
            score=score,
            reasoning=reasoning,
        )
        matches.append(match)

    MatchResult.objects.bulk_create(matches)
    return matches
