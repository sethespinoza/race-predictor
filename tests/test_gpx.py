from race_predictor.gpx import parse_gpx_to_activity
from race_predictor.models import Activity, ActivityPoint

SAMPLE_GPX = """<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="Garmin">
  <trk>
    <name>Sample Run</name>
    <trkseg>
      <trkpt lat="30.2672" lon="-97.7431">
        <ele>150.0</ele>
        <time>2026-08-02T12:00:00Z</time>
        <extensions>
          <gpxtpx:TrackPointExtension xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1">
            <gpxtpx:hr>140</gpxtpx:hr>
          </gpxtpx:TrackPointExtension>
        </extensions>
      </trkpt>
      <trkpt lat="30.2675" lon="-97.7435">
        <ele>152.5</ele>
        <time>2026-08-02T12:00:05Z</time>
        <extensions>
          <gpxtpx:TrackPointExtension xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1">
            <gpxtpx:hr>144</gpxtpx:hr>
          </gpxtpx:TrackPointExtension>
        </extensions>
      </trkpt>
    </trkseg>
  </trk>
</gpx>
"""


def test_parse_gpx_to_activity_success():
    activity = parse_gpx_to_activity(SAMPLE_GPX)

    assert isinstance(activity, Activity)
    assert len(activity.points) == 2

    pt0 = activity.points[0]
    pt1 = activity.points[1]

    assert isinstance(pt0, ActivityPoint)
    assert pt0.elapsed_seconds == 0.0
    assert pt0.distance_m == 0.0
    assert pt0.elevation_m == 150.0
    assert pt0.heart_rate_bpm == 140

    assert pt1.elapsed_seconds == 5.0
    assert pt1.distance_m > 0.0  # distance from GPS coords
    assert pt1.elevation_m == 152.5
    assert pt1.heart_rate_bpm == 144
