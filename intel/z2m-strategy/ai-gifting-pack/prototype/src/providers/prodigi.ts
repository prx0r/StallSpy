import { FulfillmentOrder, FulfillmentProvider } from "./base";
import { Quote } from "../types";

/**
 * Adapter skeleton only.
 * Wire against current Prodigi API docs and product SKUs.
 * Keep API key server-side.
 */
export class ProdigiProvider implements FulfillmentProvider {
  name = "prodigi";

  constructor(
    private apiKey: string,
    private baseUrl = "https://api.prodigi.com/v4.0"
  ) {}

  async quote(input: FulfillmentOrder): Promise<Quote> {
    // Implement with current quote/product/shipping endpoints.
    throw new Error("Prodigi quote adapter not wired yet");
  }

  async submit(input: FulfillmentOrder): Promise<{ providerOrderId: string }> {
    // POST order only after:
    // 1) payment is confirmed
    // 2) customer approved exact proof
    // 3) render QA passed
    throw new Error("Prodigi order adapter not wired yet");
  }

  async cancel(providerOrderId: string): Promise<boolean> {
    throw new Error("Prodigi cancel adapter not wired yet");
  }
}
