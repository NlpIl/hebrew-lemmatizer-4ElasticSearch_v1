package ai.korra;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class HebStemmer {
    protected String stem(String term)
    {
        String host = System.getenv("KORRA_HEB_URL");
        
        if (host == null || host.trim().isEmpty()) {
            host = "http://dicta:8000/lemmas";
        };

        System.out.println("Heb stemmer host : " +host);
        // create a client
        System.out.println("Heb stemmer input : " +term);
        var client = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_1_1)
                .build();

        // create a request
        var request = HttpRequest.newBuilder()
                .uri(URI.create(host))
                .header("accept", "*/*")
                .header("Content-Type", "text/plain;charset=UTF-8")
                .POST(HttpRequest.BodyPublishers.ofString(term))
                .build();

        // use the client to send the request
        try {
            long startTime = System.nanoTime();
            var response = client.send(request, HttpResponse.BodyHandlers.ofString());
            long endTime = System.nanoTime();
            long duration = endTime - startTime;

            long durationInMs = duration / 1000_000_000;
            System.out.println("api call to dicta run time in seconds: " + durationInMs);

            return response.body();
        } catch (Exception e) {
            return "Exception while fetching response: " + e;
        }
    }
}
