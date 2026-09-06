
import { HiveActivity } from "@mythicbee/hive-activity/react";
import { DEFAULT_BEES } from "@mythicbee/hive-activity";

export function GeneratingDadWorld() {
  return (
    <HiveActivity
      seed="mission_dad_60"
      context={{
        phase: "generate-world",
        bee: DEFAULT_BEES.find(b => b.id === "bartholomew-iii"),
        season: "christmas",
        missionTags: ["sport", "memory"],
        hooks: {
          hook: "Dad's deeply questionable weak foot",
        },
      }}
      onExposure={(event) => {
        // send to your analytics/event stream
        console.log("hive_activity_exposure", event);
      }}
    />
  );
}
