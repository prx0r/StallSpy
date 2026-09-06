declare module "motion" {
  export interface AnimationControls { stop(): void; then<TResult1 = void, TResult2 = never>(onfulfilled?: ((value: void) => TResult1 | PromiseLike<TResult1>) | null, onrejected?: ((reason: any) => TResult2 | PromiseLike<TResult2>) | null): Promise<TResult1 | TResult2>; }
  export function animate(subject: any, keyframes: any, options?: any): AnimationControls;
}
declare module "*.css";
