/**
 * MythicBee — Cloudflare Worker Proxy v2
 * Supports both Cloudflare AI and OpenCode Zen
 * Token is HERE, not in client-side code
 */

const CF_ACCOUNT = "954612afb5a97bb15dddcdc70176813d";
const CF_TOKEN = "YOUR_CLOUDFLARE_TOKEN";

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };
    if (request.method === 'OPTIONS') return new Response(null, { headers: corsHeaders });

    if (url.pathname.startsWith('/api/ai/cf/')) {
      const model = url.pathname.replace('/api/ai/cf/', '');
      try {
        const body = await request.text();
        const aiResponse = await fetch(`https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT}/ai/run/${model}`, {
          method: 'POST',
          headers: { 'Authorization': `Bearer ${CF_TOKEN}`, 'Content-Type': 'application/json' },
          body: body
        });
        const result = await aiResponse.text();
        return new Response(result, { status: aiResponse.status, headers: { ...corsHeaders, 'Content-Type': 'application/json' } });
      } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500, headers: corsHeaders });
      }
    }
    return new Response('Not found', { status: 404, headers: corsHeaders });
  }
};
