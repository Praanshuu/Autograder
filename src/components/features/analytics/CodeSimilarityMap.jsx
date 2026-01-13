import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "../../ui/card";

export default function CodeSimilarityMap({ submissions }) {
    // iframe-based view, no data processing needed


    return (
        <Card className="h-full">
            <CardHeader>
                <CardTitle>Approach Clusters (UMAP)</CardTitle>
                <CardDescription>Grouping students by solution strategy & logic.</CardDescription>
            </CardHeader>
            <CardContent className="h-[500px] p-0 overflow-hidden relative">
                <iframe
                    src="/analytics/interactive_embeddings_csl100_q1_umap.html"
                    className="w-full h-full border-0"
                    title="Code Similarity UMAP"
                />
            </CardContent>
        </Card>
    );
}
