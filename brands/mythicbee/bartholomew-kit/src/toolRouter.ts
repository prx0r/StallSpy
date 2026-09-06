import type { GiftBrief } from "./giftBrief";
import { mergeGiftBrief } from "./giftBrief";
import type { BartholomewController, Expression } from "./BartholomewController";

export interface ToolContext {
  controller: BartholomewController;
  getBrief: () => GiftBrief;
  setBrief: (brief: GiftBrief) => void;
  showProducts?: (ids: string[]) => void;
  showExample?: (id: string) => void;
  requestUpload?: (kind: "photos" | "video" | "audio", prompt?: string) => void;
}

export async function routeClientTool(name: string, args: any, ctx: ToolContext) {
  switch (name) {
    case "update_gift_brief": {
      const next = mergeGiftBrief(ctx.getBrief(), args.patch ?? {});
      ctx.setBrief(next);
      return { ok: true, status: next.status };
    }
    case "get_gift_brief": return ctx.getBrief();
    case "fly_to": {
      const el = document.getElementById(args.element_id);
      if (!el) return { ok: false, error: "unknown_element" };
      await ctx.controller.flyTo(el, args.side ?? "right");
      return { ok: true };
    }
    case "point_at": {
      const el = document.getElementById(args.element_id);
      if (!el) return { ok: false, error: "unknown_element" };
      await ctx.controller.pointAt(el);
      return { ok: true };
    }
    case "set_expression":
      ctx.controller.setExpression(args.expression as Expression);
      return { ok: true };
    case "show_products":
      ctx.showProducts?.(args.product_ids ?? []);
      return { ok: true };
    case "show_example":
      ctx.showExample?.(args.example_id);
      return { ok: true };
    case "request_upload":
      ctx.requestUpload?.(args.kind, args.prompt);
      return { ok: true };
    default:
      return { ok: false, error: "unhandled_client_tool", name };
  }
}
