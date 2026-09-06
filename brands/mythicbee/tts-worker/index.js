/**
 * MythicBee — TTS Worker
 * Uses edge-tts via HTTP API or falls back to Web Speech API
 */

export default {
  async fetch(request) {
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405, headers: corsHeaders });
    }

    try {
      const { text, voice = 'en-GB-RyanNeural' } = await request.json();

      if (!text) {
        return new Response(JSON.stringify({ error: 'Text is required' }), {
          status: 400,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      }

      // For Cloudflare Workers, we can't run Python directly
      // Instead, return the text and let the client use Web Speech API
      // Or use a different TTS service
      
      // For now, return text for client-side synthesis
      return new Response(JSON.stringify({
        success: true,
        text: text,
        voice: voice,
        method: 'client-side',
        note: 'Use Web Speech API on client for production, or edge-tts via Python backend'
      }), {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });

    } catch (err) {
      return new Response(JSON.stringify({ error: err.message }), {
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }
  }
};
