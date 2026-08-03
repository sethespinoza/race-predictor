import gpxpy
import gpxpy.gpx

from race_predictor.models import Activity, ActivityPoint


def parse_gpx_to_activity(file_content: str) -> Activity:
    """Parses GPX XML string into Activity model"""
    gpx = gpxpy.parse(file_content)

    points: list[ActivityPoint] = []
    start_time: float | None = None
    total_distance_m: float = 0.0
    prev_point: gpxpy.gpx.GPXTrackPoint | None = None

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if point.time is None:
                    continue

                point_time = point.time.timestamp()
                if start_time is None:
                    start_time = point_time

                elapsed_seconds = point_time - start_time

                # calc cumulative dist from prev GPS point
                if prev_point is not None:
                    dist_delta = point.distance_2d(prev_point)
                    if dist_delta is not None:
                        total_distance_m += dist_delta
                prev_point = point

                # get hr extension if available
                hr_val: int | None = None
                for extension in point.extensions:
                    for child in extension:
                        if child.tag.endswith("hr") and child.text is not None:
                            hr_val = int(child.text)
                            break

                points.append(
                    ActivityPoint(
                        elapsed_seconds=elapsed_seconds,
                        distance_m=total_distance_m,
                        elevation_m=point.elevation if point.elevation is not None else 0.0,
                        heart_rate_bpm=hr_val,
                    )
                )

    return Activity(points=tuple(points))
